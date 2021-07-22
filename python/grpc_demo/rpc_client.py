# import asyncio
# import grpc
# from protos import game_pb2
# from protos import game_pb2_grpc
# from rpc.agent_rpc import Agent


# async def run(agent_id="rpc_client_test_agent"):
#     channel = grpc.aio.insecure_channel("127.0.0.1:5451")
#     manage_stub = game_pb2_grpc.ManageStub(channel)
#     await manage_stub.create_agent(
#         game_pb2.createAgentRequest(agent_id=agent_id)
#     )

#     agent_stub = game_pb2_grpc.AgentStub(channel)
#     desc = await agent_stub.desc(
#         game_pb2.descRequest(agent_id=agent_id, rid="111")
#     )
#     print(desc)

# channel = grpc.aio.insecure_channel("127.0.0.1:5451")

# async def test_agent(agent_id="rpc_client_test_agent"):
#     channel2 = grpc.insecure_channel("127.0.0.1:5451")
#     manage_stub = game_pb2_grpc.ManageStub(channel2)
#     manage_stub.create_agent(
#         game_pb2.createAgentRequest(agent_id=agent_id)
#     )
#     print(f"type of create_agent function is: {type(manage_stub.create_agent)}")

#     agent = Agent(channel=channel,
#                   control_id="111",
#                   agent_id=agent_id,
#                   agent_rid="111")
#     desc = await agent.desc()
#     print(f"desc from agent_rpc: {desc}")

import asyncio
import grpc
import time
import random
from protos import test_pb2
from protos import test_pb2_grpc
from math_handler import MathHandler

channel = grpc.aio.insecure_channel("127.0.0.1:5545")
math_stub = test_pb2_grpc.mathServicesStub(channel)
async def test_grpc():
    await asyncio.sleep(random.random()+0.3)
    while True:
        msg = test_pb2.surfaceRequest(width=4, height=5)
        surface = await math_stub.surface(msg)
        await asyncio.sleep(0.1)
        #print(f"here comes {surface=}")


if __name__ == "__main__":
    # print(f"the type of function run is: {type(run)}")
    loop = asyncio.get_event_loop()
    # task = loop.create_task(run())
    # task = loop.create_task(test_agent())
    for i in range(100):
        task = loop.create_task(test_grpc())
    loop.run_forever()
    # loop.run_until_complete(task)
