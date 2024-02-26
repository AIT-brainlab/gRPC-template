# gRPC Template

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
  - [In this Repository](#in-this-repository)
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

This mode is similar to `WebSocket` where both server and client expecting a data from both side at all time.


## In this Repository

We show the three components of a `gRPC` API in `Python`.
First, someone designed the interface via a `.proto` file.
Then, both serve and client (in `Python`) compile the `.proto` using `python3 -m grpc_tools.protoc --proto_path=../protos --python_out=./services/ --grpc_python_out=./services/ ../protos/greet.proto` to compile/generate an interface in `Python` language.
Last, implement the logic.

## Resources

- Best YouTube on `Protocol Buffer` https://www.youtube.com/watch?v=46O73On0gyI&t=93s
- Best YouTube on `gRPC` https://www.youtube.com/watch?v=Yw4rkaTc0f8&t=2913s
- Best YouTube on `gRPC` in `Python` https://www.youtube.com/watch?v=WB37L7PjI5k