# rest-vs-rpc

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



