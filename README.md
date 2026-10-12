# UIT2702 — Cloud and Distributed Computing Lab Exercises

This repository contains solutions and step-by-step run instructions for all seven exercises in the Cloud and Distributed Computing lab manual.

## Folder map

1. [Exercise 01 — Inter-Process Communication](Exercise-01-IPC/QUESTION_AND_ANSWER.txt)
2. [Exercise 02 — Remote Method Invocation (Pyro4)](Exercise-02-RMI/QUESTION_AND_ANSWER.txt)
3. [Exercise 03 — Message Passing and Distributed Mutual Exclusion](Exercise-03-Message-Passing/QUESTION_AND_ANSWER.txt)
4. [Exercise 04 — Lamport and Vector Clocks](Exercise-04-Logical-Vector-Clocks/QUESTION_AND_ANSWER.txt)
5. [Exercise 05 — Virtual Instances, Consolidation and Fault Tolerance](Exercise-05-Virtual-Instances/QUESTION_AND_ANSWER.txt)
6. [Exercise 06 — Task Scheduling and Load Balancing](Exercise-06-Scheduling-Load-Balancing/QUESTION_AND_ANSWER.txt)
7. [Exercise 07 — Hypervisor Clustering](Exercise-07-Hypervisor-Clustering/QUESTION_AND_ANSWER.txt)

Each folder contains a QUESTION_AND_ANSWER.txt with the question, aim, where to perform it, setup/run steps, expected results and troubleshooting. Runnable code/config files are alongside it.

## Environment

- Exercises 1–4: Python 3 on Ubuntu. Some parts run locally in a single VM; socket/RMI demos can be extended to multiple VMs.
- Exercises 5–7: VMware Workstation Pro and Linux VMs. These are infrastructure labs, so GUI/network configuration and evidence screenshots are part of the solution, not just Python code.
- Run commands from the folder of the relevant exercise.
- Never expose test services to the public internet without authentication/firewall rules.
