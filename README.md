# gRPC Template

This document is not for teaching but is done mostly for quick reference when I come back to this project.

Table of content
---

- [gRPC Template](#grpc-template)
  - [Table of content](#table-of-content)
  - [What is `gRPC`](#what-is-grpc)
    - [Mode of operations](#mode-of-operations)
      - [Mode 1. Unary RPC](#mode-1-unary-rpc)
      - [Mode 2. Server streaming RPC](#mode-2-server-streaming-rpc)
      - [Mode 3. Client streaming RPC](#mode-3-client-streaming-rpc)
      - [Mode 4. Bidirectional streaming RPC](#mode-4-bidirectional-streaming-rpc)
  - [Step to build an API/RPC with gRPC](#step-to-build-an-apirpc-with-grpc)
    - [Protocol Buffer Compiler (protoc)](#protocol-buffer-compiler-protoc)
  - [Our Implementation](#our-implementation)
    - [Server Side](#server-side)
    - [Client Side](#client-side)
  - [Resources](#resources)



## What is `gRPC`

> [gRPC](https://grpc.io/#:~:text=gRPC%20is%20a%20modern%20open,can%20run%20in%20any%20environment.) is a modern open source high-performance Remote Procedure Call (RPC) framework that can run in any environment.

When we want to connect services over the internet, we often use `REST API`.
But, that is not the only option or even the best option.
`REST API` runs on HTTP request which makes it easy to implement on the browser.
That is fine for a basic task.

If you want to solve a real-time application where the server can be the one initiating/pushing the data without client request, you might want to choose `WebSocket`.

While we have all of those standards, `gRPC` is one standard that aims to standardize all protocols into one with multiple programming language support.

One problem with `REST API` is documentation.
How to use an API to get what you want?
`gRPC` builds upon a `protocol buffer`, thus it sends the data in binary format.
With `Protocol Buffer` you will need to define the `package`.
Both server and client will use this `Protocol Buffer` as an API reference.

The only limitation of `gRPC` is that it can not run on browsers ... yet.

### Mode of operations

[link](https://grpc.io/docs/what-is-grpc/core-concepts/)

`gRPC` has four modes of operation. 
But it is easier to think about *which side wants to stream data*.

#### Mode 1. [Unary RPC](https://grpc.io/docs/what-is-grpc/core-concepts/#unary-rpc)

This is equal to `REST API` where a client makes a single request and a server replies with a single message.

#### Mode 2. [Server streaming RPC](https://grpc.io/docs/what-is-grpc/core-concepts/#server-streaming-rpc)

A client makes a single request but this time a server replies with a stream of data.
This is good for downloading big files.

#### Mode 3. [Client streaming RPC](https://grpc.io/docs/what-is-grpc/core-concepts/#client-streaming-rpc)

A client sends a stream of data. At the end, a server replies with a single message.
This is good for uploading big files.

#### Mode 4. [Bidirectional streaming RPC](https://grpc.io/docs/what-is-grpc/core-concepts/#bidirectional-streaming-rpc)

This mode is similar to `WebSocket` where both the server and client expect data from both sides at all times.


## Step to build an API/RPC with gRPC

1. Define the service and message in `.proto`
2. Implement the login in the app following the `.proto` file


### Protocol Buffer Compiler (protoc)

When you define the services and message in `.proto` format, you will want to implement the service in your app with your programming language of choice.
The library provides you with a compiler called `protoc`.
In `Python`, you can install this tool via `pip`.

```sh
pipenv install grpc_tools
```

Then, you can call the compiler with 

```sh
python3 -m grpc_tools.protoc
```

Let's say we have all the `.proto` files in `../protos` folders. 
To generate all `.proto`, you can use this command.

```sh
# --proto_path: where the `.proto` is 
# --python_out: path to save the generated `_pb2.py` which define the proto object
# --pyi_out:    path to save the generated `_pb2.pyi` which define the interface of proto object
# --grpc_python_out: path to save the generated `_pb2_grpc.py` which define the `gRPC` interface for both Server and Client.
# The argument can be a path to either (1) single `.proto` file or (2) folder contains multiple `.proto` files.
python3 -m grpc_tools.protoc --proto_path=../protos/ --python_out=./services/ --pyi_out=./services --grpc_python_out=./services ../protos/simple.proto
```

## Our Implementation

Our implementation follows this scenario.

1. Someone defines the `gRPC` interface in `protos` folder.
2. The server and client then implement the logic on their project.
3. We simulate two different hosts via `Docker`.

### Server Side

```txt
src/
  |- services/
    |- simple_pb/
        |- simple_pb2_grpc.py
        |- simple_pb2.py
        |- simple_pb2.pyi
    |- simple.py
  |- server.py
```

To hide all the service-dependent logic, we store all the generated `pb2` files in `services/simple_pb/` and implement the gRPC interface class in `services/simple.py`.
One extra step that we have to do is change the import code in `simple_pb2_grpc.py` at line 5 from

```python
import simple_pb2 as simple__pb2
```

to

```python
from . import simple_pb2 as simple__pb2
```

The interface class in `services/simple.py` will require adding a service handler in the `__init__` function at line 8

```python
simple_pb2_grpc.add_SimpleMessageServicer_to_server(servicer=self, server=server)
```

Thus, if the server wants to add/remove services, it can do that by simply passing a `server` variable to the interface class at line 9 in `server.py`.

```python
SimpleService(server=server)
```

### Client Side

The client side is done in a similar fashion

```txt
src/
  |- services/
    |- simple_pb/
        |- simple_pb2_grpc.py
        |- simple_pb2.py
        |- simple_pb2.pyi
    |- simple.py
  |- client.py
```

However, in the real implementation, it may be difficult to hide the `pb2` object because the app has to consume it.
So the `service/simple.py` only has `get_stub()` function that creates a connection to the server (we did this because services may be served by different servers) and returns the stub.
The same `service/simple.py` file also does the necessary import of all the `pb2` files inside the `services/simple_pb` so the `client.py` does not need to dive into the package.

## Resources

- Best YouTube on `Protocol Buffer` https://www.youtube.com/watch?v=46O73On0gyI&t=93s
- Best YouTube on `gRPC` https://www.youtube.com/watch?v=Yw4rkaTc0f8&t=2913s
- Best YouTube on `gRPC` in `Python` https://www.youtube.com/watch?v=WB37L7PjI5k