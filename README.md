# Popular network communication protocols

[![lint](https://github.com/codophobia/Network-communication-protocols/actions/workflows/lint.yaml/badge.svg)](https://github.com/codophobia/Network-communication-protocols/actions/workflows/lint.yaml) [![test](https://github.com/codophobia/Network-communication-protocols/actions/workflows/test.yaml/badge.svg)](https://github.com/codophobia/Network-communication-protocols/actions/workflows/test.yaml) ![GitHub License](https://img.shields.io/github/license/codophobia/Network-communication-protocols) ![GitHub top language](https://img.shields.io/github/languages/top/codophobia/Network-communication-protocols)

Code examples in Python to understand popular network communication protocols like TCP, HTTP and RPC

## Set up
```
git clone https://github.com/codophobia/rest-vs-rpc.git
cd rest-vs-rpc
python3 -m pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running RPC client and server
```
python rpc/server.py
```
In another terminal, run the client.
```
python rpc/python_client.py
```
Generate client stubs
```
python -m grpc_tools.protoc --proto_path=rpc/proto --python_out=rpc/proto/gen/py  --pyi_out=rpc/proto/gen/py --grpc_python_out=rpc/proto/gen/py rpc/proto/calculator.proto
```

## Running REST client and server
```
python rest/server.py
```
In another terminal, run the client.
```
python rest/python_client.py
```

## Running Socket client and server
```
python socket/server.py
```
In another terminal, run the client.
```
python socket/python_client.py
```



