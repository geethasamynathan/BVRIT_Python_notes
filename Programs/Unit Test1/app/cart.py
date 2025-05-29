class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items.append((name, quantity))

    def total_items(self):
        return sum(q for _, q in self.items)