from pathlib import Path


class InventoryReport:

    def save(self, products, filename):

        path = Path(filename)

        with path.open(
            "w",
            encoding="utf8"
        ) as file:

            file.write(
                "Inventory Report\n"
            )

            file.write(
                "====================\n\n"
            )

            for product in products:

                file.write(

                    f"{product.name}"

                    f" | Qty: {product.quantity}"

                    f" | ${product.price:.2f}\n"

                )
