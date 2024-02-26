
from services import greet_pb2, greet_pb2_grpc
import time
import grpc

def get_client_stream_request():
    while True:
        name = input("Just give me your name: ")
        if name == "": break
        hello_request = greet_pb2.HelloRequest(name = name)
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:5000') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("2. SayHello - ServerStream")
        print("3. SayHello - ClientStream")
        print("4. SayHello - BiDirection")
        rpc_call = input("Which rpc you would like to call: ")

        if(rpc_call == "1"):
            hello_request = greet_pb2.HelloRequest(name="Akraradet")
            hello_reply = stub.SayHello(hello_request)
            print(f"The reply: {hello_reply}")
        elif(rpc_call == "2"):
            hello_request = greet_pb2.HelloRequest(name="Akraradet")
            hello_replies = stub.ServerStream_SayHello(hello_request)
            for hello_reply in hello_replies:
                print(f"The reply: {hello_reply}")
        elif(rpc_call == "3"):

            delayed_reply = stub.ClientStream_SayHello(get_client_stream_request())
            print(f"Reply: {delayed_reply}")

        elif(rpc_call == "4"):
            responses = stub.BiDirection_SayHello(get_client_stream_request())
            for response in responses:
                print(response)
        else:
            print("Undefined")

if __name__ == "__main__":
    run()