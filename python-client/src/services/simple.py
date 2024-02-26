import grpc
from services.simple_pb import simple_pb2, simple_pb2_grpc

def get_stub():
    channel = grpc.insecure_channel('server:5000')
    stub = simple_pb2_grpc.SimpleMessageStub(channel=channel)
    return stub