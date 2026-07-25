from config import LOW_STOCK_LIMIT

class InventoryManager:

    def total_value(

        self,

        products

    ):

        return sum(

            p.quantity * p.price

            for p in products

        )

    def total_items(

        self,

        products

    ):

        return sum(

            p.quantity

            for p in products

        )

    def low_stock(

        self,

        products

    ):

        return [

            p

            for p in products

            if p.quantity < LOW_STOCK_LIMIT

        ]
