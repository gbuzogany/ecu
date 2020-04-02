import grpc
import dash_pb2
import dash_pb2_grpc

class DashClient:
	def __init__(self, config):
		self.config = config

	def UpdateDashData(self, dashData):
		with grpc.insecure_channel('localhost:50052') as channel:
			stub = dash_pb2_grpc.DashControlStub(channel)
			response = stub.UpdateDashData(dashData)
			# print(response.status)

	def UpdateDashExtendedData(self, dashExtendedData):
		with grpc.insecure_channel('localhost:50052') as channel:
			stub = dash_pb2_grpc.DashControlStub(channel)
			response = stub.UpdateDashExtendedData(dashExtendedData)
			# print(response.status)
