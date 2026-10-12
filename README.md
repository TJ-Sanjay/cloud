# UIT2702 — Cloud and Distributed Computing Lab Exercises

Repository for all seven exercises.

## Clone the repository

    git clone https://github.com/TJ-Sanjay/cloud.git
    cd cloud

## Exercises 1–4 — Code files only

These folders contain the Python code directly. There are no extra instruction text files in these four folders.

1. [Exercise 1 — Inter-Process Communication](Exercise-01-IPC/)
   - Basic socket client/server and number summation.
   - Object transfer using pickle.
2. [Exercise 2 — Remote Method Invocation (Pyro4)](Exercise-02-RMI/)
   - Calculator server and client.
3. [Exercise 3 — Message Passing and Distributed Mutual Exclusion](Exercise-03-Message-Passing/)
   - Multi-client chat, Ricart–Agrawala simulation, Token Ring, and Centralized Coordinator.
4. [Exercise 4 — Logical and Vector Clocks](Exercise-04-Logical-Vector-Clocks/)
   - Lamport logical clock and vector clock simulations.

Run each Python program from its own exercise folder with Python 3. For Exercise 2, install Pyro4 first with `python3 -m pip install Pyro4`.

## Exercises 5–7 — One step-by-step text file per exercise

5. [Exercise 5 — Virtual Instances, Server Consolidation and Fault Tolerance](Exercise-05-Virtual-Instances/EXERCISE_5_STEPS.txt)
6. [Exercise 6 — Task Scheduling and Load Balancing](Exercise-06-Scheduling-Load-Balancing/EXERCISE_6_STEPS.txt)
7. [Exercise 7 — Hypervisor Clustering](Exercise-07-Hypervisor-Clustering/EXERCISE_7_STEPS.txt)

Each of these text files contains numbered steps, commands to run, file names to create/edit, and the complete contents to put into those files. The steps are based on the lab manual and use Ubuntu/VMware examples.

## Notes

- Replace example IP addresses and usernames with your actual lab values.
- Exercises 5 and 7 require real VMware/hypervisor configuration; a text file cannot perform those GUI steps automatically.
- Keep test services on a trusted private lab network. Pickle is unsafe for untrusted network input.
