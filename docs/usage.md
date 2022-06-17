# Usage

To use deluge-grpc ...

## Run the python gRPC server

Uses mupaduw/deluge-card to manage deluge folders on the service host.

```
python3 -m deluge_grpc.async_server
```

## Run the python client demo

Use mupaduw/deluge-card from python via gRPC.

```
python3 -m deluge_grpc.demo_client --help
```

## Run the node client demo

Use mupaduw/deluge-card from javascript via gRPC.

```
cd node_client
npm install
node demo_client.js "path/to/your/deluge/cards"
```
