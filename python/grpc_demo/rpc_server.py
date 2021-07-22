import asyncio
import grpc
from protos import test_pb2
from protos import test_pb2_grpc
from math_handler import MathHandler as MathServices


class GrpcServer():

    def __init__(self):
        pass

    async def serve(self):
        server = grpc.aio.server()
        test_pb2_grpc.add_mathServicesServicer_to_server(MathServices(),
                                                         server)
        listen_addr = "127.0.0.1:5545"
        server.add_insecure_port(listen_addr)
        await server.start()
        try:
            await server.wait_for_termination()
        except KeyboardInterrupt:
            await server.stop(0)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    grpc_server = GrpcServer()
    task = loop.create_task(grpc_server.serve())
    loop.run_until_complete(task)
