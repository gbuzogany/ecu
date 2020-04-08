# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import dash_pb2 as dash__pb2


class DashControlStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateDashData = channel.unary_unary(
                '/dash.DashControl/UpdateDashData',
                request_serializer=dash__pb2.DashData.SerializeToString,
                response_deserializer=dash__pb2.StatusResponse.FromString,
                )
        self.UpdateDashExtendedData = channel.unary_unary(
                '/dash.DashControl/UpdateDashExtendedData',
                request_serializer=dash__pb2.DashExtendedData.SerializeToString,
                response_deserializer=dash__pb2.StatusResponse.FromString,
                )


class DashControlServicer(object):
    """Missing associated documentation comment in .proto file"""

    def UpdateDashData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDashExtendedData(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DashControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateDashData': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDashData,
                    request_deserializer=dash__pb2.DashData.FromString,
                    response_serializer=dash__pb2.StatusResponse.SerializeToString,
            ),
            'UpdateDashExtendedData': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDashExtendedData,
                    request_deserializer=dash__pb2.DashExtendedData.FromString,
                    response_serializer=dash__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dash.DashControl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DashControl(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def UpdateDashData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dash.DashControl/UpdateDashData',
            dash__pb2.DashData.SerializeToString,
            dash__pb2.StatusResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDashExtendedData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dash.DashControl/UpdateDashExtendedData',
            dash__pb2.DashExtendedData.SerializeToString,
            dash__pb2.StatusResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class MediaPlayerStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PlayStatusChanged = channel.unary_unary(
                '/dash.MediaPlayer/PlayStatusChanged',
                request_serializer=dash__pb2.PlayStatus.SerializeToString,
                response_deserializer=dash__pb2.StatusResponse.FromString,
                )
        self.MediaChanged = channel.unary_unary(
                '/dash.MediaPlayer/MediaChanged',
                request_serializer=dash__pb2.MediaItem.SerializeToString,
                response_deserializer=dash__pb2.StatusResponse.FromString,
                )


class MediaPlayerServicer(object):
    """Missing associated documentation comment in .proto file"""

    def PlayStatusChanged(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MediaChanged(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MediaPlayerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PlayStatusChanged': grpc.unary_unary_rpc_method_handler(
                    servicer.PlayStatusChanged,
                    request_deserializer=dash__pb2.PlayStatus.FromString,
                    response_serializer=dash__pb2.StatusResponse.SerializeToString,
            ),
            'MediaChanged': grpc.unary_unary_rpc_method_handler(
                    servicer.MediaChanged,
                    request_deserializer=dash__pb2.MediaItem.FromString,
                    response_serializer=dash__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dash.MediaPlayer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MediaPlayer(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def PlayStatusChanged(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dash.MediaPlayer/PlayStatusChanged',
            dash__pb2.PlayStatus.SerializeToString,
            dash__pb2.StatusResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MediaChanged(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dash.MediaPlayer/MediaChanged',
            dash__pb2.MediaItem.SerializeToString,
            dash__pb2.StatusResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
