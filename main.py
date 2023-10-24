import argparse
import json
import multiprocessing
from time import sleep
from concurrent import futures
import grpc
import example_pb2_grpc
from Branch import Branch
from Customer import Customer


def serve_branch(branch):
    branch.createStubs()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_BranchServicer_to_server(branch, server)
    server.add_insecure_port("[::]:" + str(50000 + branch.id))
    server.start()
    server.wait_for_termination()


def serve_customer(customer):
    customer.createStub()
    customer.executeEvents()
    output = customer.output()
    with open("output.txt", "a") as output_file:
        output_file.write(str(output) + "\n")


def create_processes(processes):
    branches = []
    customers = []
    for process in processes:
        if process["type"] == "branch":
            branch = Branch(process["id"], process["balance"], [b.id for b in branches])
            branches.append(branch)
        elif process["type"] == "customer":
            customer = Customer(process["id"], process["events"])
            customers.append(customer)

    branch_processes = [multiprocessing.Process(target=serve_branch, args=(branch,)) for branch in branches]
    customer_processes = [multiprocessing.Process(target=serve_customer, args=(customer,)) for customer in customers]

    for branch_process in branch_processes:
        branch_process.start()
        sleep(0.25)

    for customer_process in customer_processes:
        customer_process.start()

    for customer_process in customer_processes:
        customer_process.join()

    for branch_process in branch_processes:
        branch_process.terminate()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, 'r') as file:
        input_data = json.load(file)

    with open("output.txt", "w") as output_file:
        output_file.write("")

    create_processes(input_data)
