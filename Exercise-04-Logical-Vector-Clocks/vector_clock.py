class VectorClock:
    def __init__(self, process_id, process_count):
        if not 0 <= process_id < process_count:
            raise ValueError("process_id must be between 0 and process_count - 1")
        self.process_id = process_id
        self.vector = [0] * process_count

    def event(self):
        self.vector[self.process_id] += 1
        print(f"P{self.process_id}: internal event -> {self.vector}")

    def send_message(self, receiver):
        self.vector[self.process_id] += 1
        message_vector = self.vector.copy()
        print(f"P{self.process_id} -> P{receiver.process_id}: vector={message_vector}")
        receiver.receive_message(self.process_id, message_vector)

    def receive_message(self, sender_id, sender_vector):
        if len(sender_vector) != len(self.vector):
            raise ValueError("Vector lengths must match.")
        self.vector = [max(a, b) for a, b in zip(self.vector, sender_vector)]
        self.vector[self.process_id] += 1
        print(f"P{self.process_id} received from P{sender_id} -> {self.vector}")

if __name__ == "__main__":
    p0 = VectorClock(0, 3)
    p1 = VectorClock(1, 3)
    p2 = VectorClock(2, 3)
    p0.event()
    p0.send_message(p1)
    p1.event()
    p1.send_message(p2)
    p2.event()
    p2.send_message(p0)
