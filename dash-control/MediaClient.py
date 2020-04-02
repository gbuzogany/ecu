import grpc
import dash_pb2
import dash_pb2_grpc

class MediaClient:
	def __init__(self, config):
		self.config = config

	def PlayStatusChanged(self, playStatus):
		with grpc.insecure_channel('localhost:50051') as channel:
			stub = dash_pb2_grpc.MediaPlayerStub(channel)
			response = stub.PlayStatusChanged(playStatus)
			# print(response.status)

	def MediaChanged(self, mediaItem):
		with grpc.insecure_channel('localhost:50051') as channel:
			stub = dash_pb2_grpc.MediaPlayerStub(channel)
			response = stub.MediaChanged(mediaItem)
			# print(response.status)
