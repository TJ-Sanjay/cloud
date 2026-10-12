"""Token-ring mutual exclusion simulation."""
class TokenRing:
    def __init__(self, process_ids):
        if len(process_ids) < 2:
            raise ValueError("Use at least two processes.")
        self.process_ids = list(process_ids)
        self.token_owner_index = 0
        self.in_cs = False

    def circulate(self, requests):
        requests = set(requests)
        for _ in range(len(self.process_ids) * 2):
            pid = self.process_ids[self.token_owner_index]
            print(f"Token arrives at P{pid}")
            if pid in requests:
                if self.in_cs:
                    raise RuntimeError("Mutual exclusion violated")
                self.in_cs = True
                print(f"P{pid} ENTERS critical section")
                print(f"P{pid} LEAVES critical section")
                self.in_cs = False
                requests.remove(pid)
            self.token_owner_index = (self.token_owner_index + 1) % len(self.process_ids)
            if not requests:
                break
        if requests:
            print("No token visit yet for:", sorted(requests))

if __name__ == "__main__":
    TokenRing([1, 2, 3, 4]).circulate(requests=[2, 4, 1])
