from services.simple_pb import simple_pb2, simple_pb2_grpc
import time


class SimpleService(simple_pb2_grpc.SimpleMessageServicer):
    def __init__(self, server):
        super().__init__()
        simple_pb2_grpc.add_SimpleMessageServicer_to_server(servicer=self, server=server)

    def Simple_Unary(self, request, context) -> simple_pb2.ReplyMessage:
        print(f"Simple_Unary called: {request.id=} {request.sentFrom=} {request.message=}")
        replyMessage = simple_pb2.ReplyMessage()
        replyMessage.id = request.id
        replyMessage.sentFrom = "server"
        replyMessage.message = "Recieved"
        replyMessage.requestMessage.id = request.id
        replyMessage.requestMessage.sentFrom = request.sentFrom
        replyMessage.requestMessage.message = request.message
        return replyMessage

    def Simple_ServerStream(self, request, context):
        print(f"Simple_ServerStream called: {request.id=} {request.sentFrom=} {request.message=}")
        for i in range(10):
            replyMessage = simple_pb2.ReplyMessage()
            replyMessage.id = i
            replyMessage.sentFrom = "server"
            replyMessage.message = f"Packet {i}"
            # note that I did not set requestMessage.
            yield replyMessage
            # Simulate latency
            time.sleep(1)

    def Simple_ClientStream(self, request_iterator, context) -> simple_pb2.ReplyMessage:
        print(f"Simple_ClientStream called")
        number_of_message = 0
        for request in request_iterator:
            print(f"Client sent: {request.id=} {request.sentFrom=} {request.message=}")
            number_of_message += 1
        replyMessage = simple_pb2.ReplyMessage()
        replyMessage.id = request.id
        replyMessage.sentFrom = "server"
        replyMessage.message = f"Recieved {number_of_message} messages"
        replyMessage.requestMessage.id = request.id
        replyMessage.requestMessage.sentFrom = request.sentFrom
        replyMessage.requestMessage.message = request.message
        return replyMessage

    def Simple_BiDirection(self, request_iterator, context):
        print(f"Simple_BiDirection called")
        count = 0
        for request in request_iterator:
            print(f"Client sent: {request.id=} {request.sentFrom=} {request.message=}")
            count += 1
            if(count % 5 == 0):
                replyMessage = simple_pb2.ReplyMessage()
                replyMessage.id = request.id
                replyMessage.sentFrom = "server"
                replyMessage.message = f"Got {count} messages in total"
                replyMessage.requestMessage.id = request.id
                replyMessage.requestMessage.sentFrom = request.sentFrom
                replyMessage.requestMessage.message = request.message
                yield replyMessage
        # print(f"Simple_BiDirection called: {request.id=} {request.sentFrom=} {request.message=}")
        # return super().Simple_BiDirection(request=request_iterator, context=context)
