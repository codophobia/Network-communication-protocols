import sys
sys.path.append('rpc/proto/gen/py')

import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorService):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.Response(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_service = CalculatorServicer()
    calculator_pb2_grpc.add_CalculatorServiceServicer_to_server(
        calculator_service, server)
    server.add_insecure_port('[::]:50051')
    print('Starting server. Listening on port 50051.')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
