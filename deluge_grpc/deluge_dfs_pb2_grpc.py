# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import deluge_dfs_pb2 as deluge__dfs__pb2
import grpc


class DelugeFolderSystemStub(object):
    """The service definition."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFolderSystems = channel.unary_unary(
            '/deluge_dfs.DelugeFolderSystem/ListFolderSystems',
            request_serializer=deluge__dfs__pb2.ListFoldersRequest.SerializeToString,
            response_deserializer=deluge__dfs__pb2.ListFoldersReply.FromString,
        )
        self.ListContents = channel.unary_unary(
            '/deluge_dfs.DelugeFolderSystem/ListContents',
            request_serializer=deluge__dfs__pb2.ListContentsRequest.SerializeToString,
            response_deserializer=deluge__dfs__pb2.ListContentsReply.FromString,
        )


class DelugeFolderSystemServicer(object):
    """The service definition."""

    def ListFolderSystems(self, request, context):
        """Sends a list of folders that appear to be Deluge FS"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListContents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DelugeFolderSystemServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ListFolderSystems': grpc.unary_unary_rpc_method_handler(
            servicer.ListFolderSystems,
            request_deserializer=deluge__dfs__pb2.ListFoldersRequest.FromString,
            response_serializer=deluge__dfs__pb2.ListFoldersReply.SerializeToString,
        ),
        'ListContents': grpc.unary_unary_rpc_method_handler(
            servicer.ListContents,
            request_deserializer=deluge__dfs__pb2.ListContentsRequest.FromString,
            response_serializer=deluge__dfs__pb2.ListContentsReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler('deluge_dfs.DelugeFolderSystem', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DelugeFolderSystem(object):
    """The service definition."""

    @staticmethod
    def ListFolderSystems(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/deluge_dfs.DelugeFolderSystem/ListFolderSystems',
            deluge__dfs__pb2.ListFoldersRequest.SerializeToString,
            deluge__dfs__pb2.ListFoldersReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListContents(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/deluge_dfs.DelugeFolderSystem/ListContents',
            deluge__dfs__pb2.ListContentsRequest.SerializeToString,
            deluge__dfs__pb2.ListContentsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
