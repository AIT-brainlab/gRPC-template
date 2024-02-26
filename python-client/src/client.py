from services.simple import get_stub, simple_pb2
import time

def message_generator():
    for i in range(10):
        message = f"Hi Server!!! This is message {i}"
        requestMessage = simple_pb2.RequestMessage(id=i, sentFrom="client", message=message)
        yield requestMessage
        # simulate latency
        time.sleep(1)

def simple_unary_call():
    requestMessage = simple_pb2.RequestMessage(id=1, sentFrom="client", message="Hi Server")
    stub = get_stub()
    reply = stub.Simple_Unary(requestMessage)
    print(f"Server Reply: {reply}")

def simple_serverstream_call():
    requestMessage = simple_pb2.RequestMessage(id=1, sentFrom="client", message="Hi Server")    
    stub = get_stub()
    replies = stub.Simple_ServerStream(requestMessage)
    for reply in replies:
        print(f"Server Reply: {reply}")

def simple_clientstream_call():
    stub = get_stub()
    reply = stub.Simple_ClientStream(message_generator())
    print(f"Server Reply: {reply}")


def simple_bidirection_call():
    stub = get_stub()
    replies = stub.Simple_BiDirection(message_generator())
    for reply in replies:
        print(f"Server Reply: {reply}")

def run():
    print(f"1. Simple_Unary")
    print(f"2. Simple_ServerStream")
    print(f"3. Simple_ClientStream")
    print(f"4. Simple_BiDirection")
    call_id = input(f"Select what function you want to try: ")
    if(call_id == "1"):
        simple_unary_call()
    elif(call_id == "2"):
        simple_serverstream_call()
    elif(call_id == "3"):
        simple_clientstream_call()
    elif(call_id == "4"):
        simple_bidirection_call()
    else:
        print("Not implemented")

if __name__ == "__main__":
    run()
    