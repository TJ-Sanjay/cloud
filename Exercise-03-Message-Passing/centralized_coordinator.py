"""Centralized-coordinator mutual exclusion simulation using a FIFO queue."""
from collections import deque

class Coordinator:
    def __init__(self):
        self.queue = deque()
        self.owner = None

    def request(self, pid):
        print(f"P{pid} -> Coordinator: REQUEST_CS")
        self.queue.append(pid)
        self.grant_next()

    def grant_next(self):
        if self.owner is None and self.queue:
            self.owner = self.queue.popleft()
            print(f"Coordinator -> P{self.owner}: GRANT_CS")
            self.enter_and_release(self.owner)

    def enter_and_release(self, pid):
        if self.owner != pid:
            raise RuntimeError("Only the current owner may enter the critical section.")
        print(f"P{pid} ENTERS critical section")
        print(f"P{pid} -> Coordinator: RELEASE_CS")
        self.owner = None
        self.grant_next()

if __name__ == "__main__":
    coordinator = Coordinator()
    for process_id in [2, 1, 3, 2]:
        coordinator.request(process_id)
    print("All queued requests processed.")
