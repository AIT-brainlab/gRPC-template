from concurrent import futures
import time

import grpc
from services import greet_pb2, greet_pb2_grpc

class GreetService(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f"SayHello Request Made: {request}")
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.name}"
        # return super().SayHello(request=request, context=context)
        return hello_reply

    def ServerStream_SayHello(self, request, context):
        print("ServerStream: ")
        print(request)
        for i in range(10):
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{request.name} {i}"
            yield hello_reply
            time.sleep(1)
        

    def ClientStream_SayHello(self, request_iterator, context):
        delayed_reply = greet_pb2.DelayedReply()
        for request in request_iterator:
            print(f"ClentStream: {request}")
            delayed_reply.request.append(request)
        delayed_reply.message = f"You have sent {len(delayed_reply.request)}."
        return delayed_reply
    
    def BiDirection_SayHello(self, request_iterator, context):
        for request in request_iterator:
            print(f"Bidirection: {request}")
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{request.name} from server"
            yield hello_reply

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(servicer=GreetService(), server=server)
    server.add_insecure_port("0.0.0.0:5000")
    server.start()
    server.wait_for_termination()