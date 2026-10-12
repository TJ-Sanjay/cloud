"""Deterministic single-machine simulation of Ricart-Agrawala mutual exclusion."""
from dataclasses import dataclass

@dataclass
class Request:
    pid: int
    timestamp: int

class RicartAgrawalaSimulation:
    def __init__(self, process_ids):
        self.process_ids = list(process_ids)
        self.clock = {pid: 0 for pid in self.process_ids}
        self.requesting = set()
        self.deferred = {pid: [] for pid in self.process_ids}
        self.in_cs = None

    def request_cs(self, pid):
        self.clock[pid] += 1
        request = Request(pid, self.clock[pid])
        self.requesting.add(pid)
        print(f"P{pid} broadcasts REQUEST ts={request.timestamp}")
        replies = []
        for peer in self.process_ids:
            if peer == pid:
                continue
            self.clock[peer] = max(self.clock[peer], request.timestamp) + 1
            peer_request = Request(pid, request.timestamp)
            # In this deterministic demonstration, lower (timestamp, PID) priority wins.
            if peer in self.requesting:
                peer_priority = (self.clock[peer], peer)
                requester_priority = (peer_request.timestamp, pid)
                if peer_priority < requester_priority:
                    self.deferred[peer].append(pid)
                    print(f"P{peer} defers REPLY to P{pid}")
                    continue
            replies.append(peer)
            print(f"P{peer} -> P{pid}: REPLY")
        if len(replies) == len(self.process_ids) - 1:
            self.enter_cs(pid)
        else:
            print(f"P{pid} waits for deferred replies in a full distributed run.")

    def enter_cs(self, pid):
        if self.in_cs is not None:
            raise RuntimeError(f"Mutual exclusion violated: P{self.in_cs} and P{pid}")
        self.in_cs = pid
        print(f"P{pid} ENTERS critical section")
        print(f"P{pid} LEAVES critical section")
        self.in_cs = None
        self.requesting.discard(pid)
        for waiting_pid in self.deferred[pid]:
            print(f"P{pid} -> P{waiting_pid}: deferred REPLY")
        self.deferred[pid].clear()

if __name__ == "__main__":
    sim = RicartAgrawalaSimulation([1, 2, 3])
    sim.request_cs(1)
    sim.request_cs(2)
    sim.request_cs(3)
    print("Simulation completed; no overlapping critical-section entries occurred.")
