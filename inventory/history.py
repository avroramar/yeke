from datetime import datetime


class InventoryHistory:

    def __init__(self):

        self.records = []

    def add(self, product, quantity, action):

        self.records.append({

            "timestamp": datetime.now(),

            "product": product,

            "quantity": quantity,

            "action": action

        })

    def all(self):

        return self.records

    def total_events(self):

        return len(self.records)
