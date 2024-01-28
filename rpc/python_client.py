import sys
sys.path.append('rpc/proto/gen/py')

import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    # Connect to the gRPC server
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorServiceStub(channel)

    try:
        request = calculator_pb2.Request(num1=20, num2=10)
        print("Request:", request.num1, "+", request.num2)
        response = stub.Add(request)
        print("Result:", response.result)
    except grpc.RpcError as e:
        print(e.details())
        print(e.code())        


if __name__ == '__main__':
    run()
