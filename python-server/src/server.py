import grpc
from services.simple import SimpleService

from concurrent import futures
import time

def runServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    SimpleService(server=server)
    print("Server will start at 0.0.0.0 port 5000")
    server.add_insecure_port("0.0.0.0:5000")
    server.start()
    print("Server start")
    server.wait_for_termination()

if __name__ == "__main__":
    runServer()