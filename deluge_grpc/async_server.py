"""The Python AsyncIO implementation of the GRPC deluge_dfs.DelugeFolderSystem server."""

import asyncio

# import functools
import logging

# import time
from pathlib import Path

import deluge_dfs_pb2
import deluge_dfs_pb2_grpc
import grpc
from deluge_card import DelugeCardFS, list_deluge_fs

# @functools.lru_cache
# def card_songs_matching(card, pattern):
#     return list(card.songs(pattern))

# @functools.lru_cache
# def card_samples_matching(card, pattern):
#     return list(card.samples(pattern))


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

    # async def ListContents(
    #     self, request: deluge_dfs_pb2.ListContentsRequest, context: grpc.aio.ServicerContext
    # ) -> deluge_dfs_pb2.ListContentsReply:
    #     """List contents."""
    #     logging.info(f'ListContents request {request}')
    #     card = DelugeCardFS(Path(request.card_root))

    #     if request.content_type == deluge_dfs_pb2.ContentType.SONG:
    #         #res = card_songs_matching(card, request.pattern)
    #         res = card.songs(pattern)
    #     elif request.content_type == deluge_dfs_pb2.ContentType.SAMPLE:
    #         #res = card_samples_matching(card, request.pattern)
    #         res = card.samples(request.pattern)
    #     else:
    #         return
    #     return deluge_dfs_pb2.ListContentsReply(
    #         card_root=request.card_root,
    #         content_type=request.content_type,
    #         file_names=map(lambda content: str(content.path.relative_to(Path(request.card_root))), res),
    #     )

    # Streaming method
    # based on https://github.com/grpc/grpc/blob/master/examples/python/data_transmission/server.py
    #
    def ListContentsStream(self, request: deluge_dfs_pb2.ListContentsRequest, context: grpc.aio.ServicerContext):
        """List contents."""
        logging.info(f'ListContents request (streaming) {request}')
        card = DelugeCardFS(Path(request.card_root))

        if request.content_type == deluge_dfs_pb2.ContentType.SONG:
            res = card.songs(request.pattern)
        elif request.content_type == deluge_dfs_pb2.ContentType.SAMPLE:
            res = card.samples(request.pattern)
        else:
            res = []

        def responses(res, request):
            for content in res:
                response = deluge_dfs_pb2.ListContentsStreamReply(
                    file_name=str(content.path.relative_to(Path(request.card_root)))
                )
                yield response

        return responses(res, request)


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
