from concurrent import futures
import grpc
import example_pb2_grpc
from example_pb2 import MsgRequest, MsgResponse


class Branch(example_pb2_grpc.BranchServicer):
    def __init__(self, id, balance, branches):
        self.id = id
        self.balance = balance
        self.branches = branches
        self.stubList = list()
        self.recvMsg = list()

    # Setup
    def createStubs(self):
        for branchId in self.branches:
            if branchId != self.id:
                channel = grpc.insecure_channel("localhost:" + str(50000 + branchId))
                self.stubList.append(example_pb2_grpc.BranchStub(channel))

    def MsgDelivery(self, request, context):
        return self.ProcessMsg(request, True)

    def MsgPropagation(self, request, context):
        return self.ProcessMsg(request, False)

    def ProcessMsg(self, request, propagate):
        result = "success"

        if request.money < 0:
            result = "fail"
        elif request.interface == "query":
            pass
        elif request.interface == "deposit":
            self.balance += request.money
            if propagate == True:
                self.Propagate_Deposit(request)
        elif request.interface == "withdraw":
            if self.balance >= request.money:
                self.balance -= request.money
                if propagate == True:
                    self.Propagate_Withdraw(request)
            else:
                result = "fail"
        else:
            result = "fail"

        msg = {"interface": request.interface, "result": result}

        if request.interface == "query":
            msg["money"] = request.money

        self.recvMsg.append(msg)

        return MsgResponse(interface=request.interface, result=result, money=self.balance)

    def Propagate_Withdraw(self, request):
        for stub in self.stubList:
            stub.MsgPropagation(MsgRequest(id=request.id, interface="withdraw", money=request.money))

    def Propagate_Deposit(self, request):
        for stub in self.stubList:
            stub.MsgPropagation(MsgRequest(id=request.id, interface="deposit", money=request.money))