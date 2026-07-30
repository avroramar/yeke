class Pricing:

    @staticmethod
    def inventory_value(products):

        total = 0

        for product in products:

            total += (
                product.price *
                product.quantity
            )

        return round(total, 2)

    @staticmethod
    def average_price(products):

        if not products:
            return 0

        return round(

            sum(
                p.price for p in products
            ) / len(products),

            2

        )
