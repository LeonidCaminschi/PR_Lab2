# PR_Lab2

All of the code writen in here was inspired from:
https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/

## Problems
  - syntax used on the website for protobuf is syntax = "proto3" but later on compiles to proto2 ?????
  - needed a specific version of protobuf of <=3.20.1 cringe ???
  - Class in the proto file is an enum -_- needed to check the compiled proto.py file to see all the functions available so that it works as intended.

## How to run
  ```
  sudo apt install protobuf-compiler
  protoc -I=. --python_out=. ./player.proto
  pip3 install <--upgrade> "protobuf<=3.20.1"
  python3 tests.py
  python3 htests.py
  ```
  
Yours Truly,
Caminschi Leonid FAF-211
