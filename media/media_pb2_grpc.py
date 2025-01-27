# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import media_pb2 as media__pb2


class MediaPlayerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PlayStatusChanged = channel.unary_unary(
        '/mediaplayer.MediaPlayer/PlayStatusChanged',
        request_serializer=media__pb2.PlayStatus.SerializeToString,
        response_deserializer=media__pb2.StatusResponse.FromString,
        )
    self.MediaChanged = channel.unary_unary(
        '/mediaplayer.MediaPlayer/MediaChanged',
        request_serializer=media__pb2.MediaItem.SerializeToString,
        response_deserializer=media__pb2.StatusResponse.FromString,
        )


class MediaPlayerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PlayStatusChanged(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MediaChanged(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MediaPlayerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PlayStatusChanged': grpc.unary_unary_rpc_method_handler(
          servicer.PlayStatusChanged,
          request_deserializer=media__pb2.PlayStatus.FromString,
          response_serializer=media__pb2.StatusResponse.SerializeToString,
      ),
      'MediaChanged': grpc.unary_unary_rpc_method_handler(
          servicer.MediaChanged,
          request_deserializer=media__pb2.MediaItem.FromString,
          response_serializer=media__pb2.StatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mediaplayer.MediaPlayer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
