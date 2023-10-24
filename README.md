# Distributed-Banking-System
## Problem Statement
To enable secure deposit and withdrawal transactions across multiple branches, ensuring synchronized and consistent data replication while maintaining customer- specific branch interactions.

## Goal
The goal of this project is to build a distributed banking system that allows multiple customers to withdraw or deposit money from multiple branches in the bank. We assume that all the customers share the same bank account and each customer accesses only one specific branch. In this project, we also assume that there are no concurrent updates on the bank account. Each branch maintains a replica of the money that needs to be consistent with the replicas in other branches. The customer communicates with only a specific branch that has the same unique ID as the customer. Although each customer independently updates a specific replica, the replicas stored in each branch need to reflect all
the updates made by the customer.

## Objectives
● Define a service in a .proto file.
● Generate server and client code using the protocol buffer compiler.
● Use the Python gRPC API to write a simple client and server for your service. ● Build a distributed system that meets specific criteria.
● Determine the problem statement.
● Identify the goal of the problem statement.
● List relevant technologies for the setup and their versions.
● Explain the implementation processes.
● Explain implementation results.
