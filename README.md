# UIT2702 — Cloud and Distributed Computing Lab Exercises

Repository for all seven exercises.

## Clone the repository

    git clone https://github.com/TJ-Sanjay/cloud.git
    cd cloud

## Exercises 1–4 — Code files

Exercises 1, 2, and 4 use the code from the supplied `demo.zip`. Exercise 3 remains in its existing folder because it was not included in that ZIP.

1. [Exercise 1 — Socket communication and object transfer](Exercise-01-IPC/)
   - `server.py` + `client.py`: send numbers as text and return their sum.
   - `server2.py` + `client2.py`: send a pickled `DataObject` and return the sum of its values.
   - Both examples use port `12345`; run only one server example at a time.
2. [Exercise 2 — Remote Method Invocation (Pyro4)](Exercise-02-RMI/)
   - Run `server.py), copy the printed URI, then enter it in `client.py`.
   - Install Pyro4 first: `python -m pip install Pyro4`.
3. [Exercise 3 — Message Passing and Distributed Mutual Exclusion](Exercise-03-Message-Passing/)
   - Multi-client chat, Ricart–Agrawala simulation, Token Ring, and Centralized Coordinator.
4. [Exercise 4 — Logical and Vector Clocks](Exercise-04-Logical-Vector-Clocks/)
   - Original Lamport and vector clock examples from the ZIP.

Run Python files from their own exercise folder using Python 3. For the object-transfer example, run `server2.py` before `client2.py`. Only deserialize pickle data from a trusted client because pickle is unsafe for untrusted input.

## Exercises 5–7 — One step-by-step text file per exercise

5. [Exercise 5 — Virtual Instances, Server Consolidation and Fault Tolerance](Exercise-05-Virtual-Instances/EXERCISE_5_STEPS.txt)
6. [Exercise 6 — Task Scheduling and Load Balancing](Exercise-06-Scheduling-Load-Balancing/EXERCISE_6_STEPS.txt)
7. [Exercise 7 — Hypervisor Clustering](Exercise-07-Hypervisor-Clustering/EXERCISE_7_STEPS.txt)

Each text file contains numbered steps, commands to run, filenames to create/edit, and complete configuration/code where applicable. The steps use Ubuntu/VMware examples.

## Notes

- Replace example IP addresses and usernames with your actual lab values.
- Exercises 5 and 7 require real VMware/hypervisor configuration; a text file cannot perform those GUI steps automatically.
