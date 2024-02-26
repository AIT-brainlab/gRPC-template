# gRPC Template

Table of content
---

- [gRPC Template](#grpc-template)
  - [Table of content](#table-of-content)
  - [What is `gRPC`](#what-is-grpc)
  - [In this Repository](#in-this-repository)
  - [To use this Repository](#to-use-this-repository)
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

## In this Repository

We show the three components of a `gRPC` API in `Python`.
First, someone designed the interface via a `.proto` file.
Then, both serve and client (in `Python`) compile the `.proto` using `python3 -m grpc_tools.protoc --proto_path=../protos --python_out=./services/ --grpc_python_out=./services/ ../protos/greet.proto` to compile/generate an interface in `Python` language.
Last, implement the logic.

## To use this Repository

1. Create a `grpc` network as a bridge in your docker environment.
2. Run `docker compose up` to spawn server and client.


## Resources

- Best YouTube on `Protocal Buffer` https://www.youtube.com/watch?v=46O73On0gyI&t=93s
- Best YouTube on `gRPC` https://www.youtube.com/watch?v=Yw4rkaTc0f8&t=2913s
- Best YouTube on `gRPC` in `Python` https://www.youtube.com/watch?v=WB37L7PjI5k