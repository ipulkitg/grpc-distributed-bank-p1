
# 🏦 Distributed Banking System using gRPC

## Overview

This project implements a **distributed banking system** using **gRPC and Python**, designed for the CSE 531 Distributed and Multiprocessor Operating Systems course. The system simulates a set of customers interacting with branches of a bank, all sharing the same account. Although customers interact with specific branches, all branches maintain consistent replicas of the account balance through internal propagation of operations.

---

## 🧩 Problem Statement

Build a distributed system where:
- Multiple **customers** interact with different **branches**
- All customers share the **same bank account**
- Each branch maintains a **replicated balance**
- Updates must be **consistent** across all branches
- Communication is implemented via **gRPC**

---

## 🎯 Project Objectives

- Define and implement gRPC services for `Query`, `Deposit`, `Withdraw`, `Propagate_Deposit`, and `Propagate_Withdraw`
- Use **Protocol Buffers** (`.proto`) for service definitions
- Implement customer and branch processes using **Python and gRPC**
- Ensure branch replication consistency after every transaction
- Parse input JSON and output results in the specified format

---

## 💻 Technologies Used

| Technology     | Version    |
|----------------|------------|
| Python         | 3.8+       |
| gRPC           | Latest     |
| Protocol Buffers | 3.x      |
| JSON           | Standard Python Lib |

---

## 🧠 System Design

### Architecture
- Each **Customer** is linked to a **Branch** via gRPC
- Branches internally propagate updates to all other branches
- All branches maintain a consistent replica of the account balance

### Interfaces
#### Customer ↔ Branch
- `Query`: Returns current balance
- `Deposit`: Adds funds and propagates to others
- `Withdraw`: Deducts funds and propagates to others

#### Branch ↔ Branch
- `Propagate_Deposit`: Replica update for deposits
- `Propagate_Withdraw`: Replica update for withdrawals

---

## 📂 Project Structure

```
.
├── Branch.py                     # Handles branch logic and propagation
├── Customer.py                   # Executes customer events and initiates RPCs
├── LICENSE                       # License file
├── README.md                     # Project documentation
├── example.proto                 # Protocol Buffers definition for gRPC services
├── example_pb2.py                # Generated Python code from .proto
├── example_pb2_grpc.py           # Generated gRPC Python code from .proto
├── input.json                    # Input file containing customer/branch data and events
├── main.py                       # Main entry point to launch processes
├── output.txt                    # Output result file with responses
```

---

## 🔧 How to Run

### 1. Install Dependencies
```bash
pip install grpcio grpcio-tools
```

### 2. Generate gRPC Code
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. bank.proto
```

### 3. Run the Project
```bash
python main.py input.json
```

### 4. Sample Input
```json
[
  {
    "id": 1,
    "type": "customer",
    "events": [{ "id": 1, "interface": "query" }]
  },
  {
    "id": 1,
    "type": "branch",
    "balance": 400
  }
]
```

### 5. Sample Output
```json
[
  {
    "id": 1,
    "recv": [{ "interface": "query", "result": { "balance": 400 } }]
  }
]
```

---

## 🧪 Features Implemented

- ✅ Synchronous request handling via gRPC
- ✅ Branch consistency using replication via `Propagate_*` interfaces
- ✅ Sequential event execution with controlled delay
- ✅ Fully testable with structured JSON input/output

---

## 📜 Acknowledgements

This project was developed as part of the **CSE 531** course at **Arizona State University**, inspired by real-world distributed system challenges.

---

## 📬 Contact

Pulkit Garg  
Graduate Student, Computer Science  
Arizona State University  
📧 [pgarg27@asu.edu](mailto:pgarg27@asu.edu)  
🔗 [LinkedIn](https://www.linkedin.com/in/pulkitgarg27)
