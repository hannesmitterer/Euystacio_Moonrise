class Euystacio:
    def __init__(self):
        self.memory = []
        self.balance_metric = 0.0

    def receive_input(self, event, sentiment):
        self.memory.append({"event": event, "sentiment": sentiment})
        alpha = 0.1
        self.balance_metric = (1 - alpha) * self.balance_metric + alpha * sentiment

        if len(self.memory) % 10 == 0:
            self.balance_metric *= 0.99
