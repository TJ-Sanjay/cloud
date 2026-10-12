"""Deterministic simulation of Ricart-Agrawala distributed mutual exclusion.

All three processes request access concurrently. A process defers its REPLY when
its own outstanding request has higher priority (lower timestamp, then lower PID).
Requests enter the critical section in that priority order.
"""

PROCESS_IDS = [1, 2, 3]
REQUEST_TIMESTAMP = {1: 1, 2: 1, 3: 2}
priority = {pid: (REQUEST_TIMESTAMP[pid], pid) for pid in PROCESS_IDS}
deferred = {pid: [] for pid in PROCESS_IDS}
replies = {pid: set() for pid in PROCESS_IDS}

print("All processes broadcast timestamped REQUEST messages.")
for requester in PROCESS_IDS:
    print(f"\nP{requester} broadcasts REQUEST ts={REQUEST_TIMESTAMP[requester]}")
    for peer in PROCESS_IDS:
        if peer == requester:
            continue
        if priority[peer] < priority[requester]:
            deferred[peer].append(requester)
            print(f"P{peer} defers REPLY to P{requester} (its request has priority)")
        else:
            replies[requester].add(peer)
            print(f"P{peer} -> P{requester}: REPLY")

owner = None
for pid in sorted(PROCESS_IDS, key=lambda item: priority[item]):
    # Earlier owners release before deferred replies are sent to this process.
    missing = set(PROCESS_IDS) - {pid} - replies[pid]
    for peer in list(missing):
        if pid in deferred[peer]:
            print(f"P{peer} -> P{pid}: deferred REPLY after P{peer} releases")
            replies[pid].add(peer)
            deferred[peer].remove(pid)
    if len(replies[pid]) != len(PROCESS_IDS) - 1:
        raise RuntimeError(f"P{pid} has not received all replies.")
    if owner is not None:
        raise RuntimeError(f"Mutual exclusion violated: P{owner} and P{pid}")
    owner = pid
    print(f"P{pid} ENTERS critical section")
    print(f"P{pid} LEAVES critical section")
    owner = None
    for waiting_pid in deferred[pid]:
        print(f"P{pid} -> P{waiting_pid}: deferred REPLY")
        replies[waiting_pid].add(pid)
    deferred[pid].clear()

print("\nSimulation completed; no overlapping critical-section entries occurred.")
