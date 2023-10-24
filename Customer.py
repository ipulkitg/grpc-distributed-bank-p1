from time import sleep

import grpc

import example_pb2_grpc
from example_pb2 import MsgRequest


class Customer:
    def __init__(self, id, events):
        self.id = id
        self.events = events
        self.recvMsg = list()
        self.stub = None

    # Setup
    def createStub(self):
        channel = grpc.insecure_channel("localhost:" + str(50000 + self.id))
        self.stub = example_pb2_grpc.BranchStub(channel)

    # Send gRPC request for each event
    def executeEvents(self):
        for event in self.events:
            # Sleep 3 seconds for 'query' events
            if event["interface"] == "query":
                sleep(3)

            # Send request to Branch server
            response = self.stub.MsgDelivery(
                MsgRequest(id=event["id"], interface=event["interface"], money=event.get('money',0))
            )

            # Create msg to be appended to self.recvMsg list
            msg = {"interface": response.interface, "result": response.result}

            # Add 'money' entry for 'query' events
            if response.interface == "query":
                msg["money"] = response.money

            self.recvMsg.append(msg)

    # Generate output msg
    def output(self):
        return {"id": self.id, "recv": self.recvMsg}