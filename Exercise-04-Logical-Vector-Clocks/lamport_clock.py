class LamportClock:
    def __init__(self, process_id):
        self.process_id = process_id
        self.clock = 0

    def event(self):
        self.clock += 1
        print(f"P{self.process_id}: internal event, timestamp={self.clock}")

    def send_message(self, receiver):
        self.clock += 1
        timestamp = self.clock
        print(f"P{self.process_id} -> P{receiver.process_id}: message timestamp={timestamp}")
        receiver.receive_message(self.process_id, timestamp)

    def receive_message(self, sender_id, sender_timestamp):
        self.clock = max(self.clock, sender_timestamp) + 1
        print(f"P{self.process_id} received from P{sender_id}, updated timestamp={self.clock}")

if __name__ == "__main__":
    p1 = LamportClock(1)
    p2 = LamportClock(2)
    p1.event()
    p1.send_message(p2)
    p2.event()
    p2.send_message(p1)
