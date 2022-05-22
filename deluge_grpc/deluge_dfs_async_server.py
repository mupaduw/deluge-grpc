"""The Python AsyncIO implementation of the GRPC deluge_dfs.DelugeFolderSystem server."""

import asyncio
import logging
from pathlib import Path

import deluge_dfs_pb2
import deluge_dfs_pb2_grpc
import grpc
from deluge_card import DelugeCardFS, list_deluge_fs


class DelugeFolderSystem(deluge_dfs_pb2_grpc.DelugeFolderSystemServicer):
    """Main entry point."""

    async def ListFolderSystems(
        self, request: deluge_dfs_pb2.ListFoldersRequest, context: grpc.aio.ServicerContext
    ) -> deluge_dfs_pb2.ListFoldersReply:
        """ListFolderSystems."""
        logging.info(f'ListFolders request {request}')
        card_imgs = list_deluge_fs(request.path)
        return deluge_dfs_pb2.ListFoldersReply(
            folder_names=[str(c.card_root.relative_to(request.path)) for c in card_imgs]
        )

    async def ListContents(
        self, request: deluge_dfs_pb2.ListContentsRequest, context: grpc.aio.ServicerContext
    ) -> deluge_dfs_pb2.ListContentsReply:
        """List contents."""
        logging.info(f'ListContents request {request}')
        card = DelugeCardFS(Path(request.card_root))

        if request.content_type == deluge_dfs_pb2.ContentType.SONG:
            res = card.songs(request.pattern)
        return deluge_dfs_pb2.ListContentsReply(
            card_root=request.card_root,
            content_type=request.content_type,
            file_names=map(lambda song: str(song.path.relative_to(Path(request.card_root))), res),
        )


async def serve() -> None:
    """Serve the service."""
    server = grpc.aio.server()
    deluge_dfs_pb2_grpc.add_DelugeFolderSystemServicer_to_server(DelugeFolderSystem(), server)
    listen_addr = '[::]:50057'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
