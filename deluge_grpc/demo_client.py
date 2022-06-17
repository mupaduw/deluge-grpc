"""Demo python gRPC client."""

import argparse
import logging

import deluge_dfs_pb2
import deluge_dfs_pb2_grpc
import grpc


def run(args):
    """Run the user command."""
    with grpc.insecure_channel('localhost:50057') as channel:
        stub = deluge_dfs_pb2_grpc.DelugeFolderSystemStub(channel)

        if args.type == 'cards':
            request = deluge_dfs_pb2.ListFoldersRequest(path=args.root)
            response = stub.ListFolderSystems(request)
            print("DelugeFolderSystem client received: " + str([s for s in response.folder_names]))

        if args.type == 'songs':
            request = deluge_dfs_pb2.ListContentsRequest(
                card_root=args.root, pattern=args.pattern or "", content_type=deluge_dfs_pb2.ContentType.SONG
            )
            response = stub.ListContents(request)
            print("DelugeFolderSystem client received: " + str([s for s in response.file_names]))

        if args.type == 'samples':
            request = deluge_dfs_pb2.ListContentsRequest(
                card_root=args.root, pattern=args.pattern or "", content_type=deluge_dfs_pb2.ContentType.SAMPLE
            )
            for r in stub.ListContentsStream(request):
                print(r.file_name)


if __name__ == '__main__':
    """e.g.\n
    > python3 demo_client.py cards /Users/chrisbc/Music/DELUGE \n
    > python3 demo_client.py cards /Users/chrisbc/Music/DELUGE/01 -p **/*10.*
    """
    logging.basicConfig()
    parser = argparse.ArgumentParser(description='demo_client.py - list Deluge FS contents via gRPC')
    parser.add_argument('type', help='one of of songs, cards, samples, future: k=kits, i=instruments.')
    parser.add_argument('root', help='root folder to begin ls from')
    parser.add_argument('-p', '--pattern', help='pattern')
    args = parser.parse_args()

    run(args)
