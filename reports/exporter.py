class Exporter:

    def save(

        self,

        products,

        summary,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write("Inventory Report\n\n")

            for product in products:

                file.write(

                    f"{product.name} "

                    f"({product.quantity}) "

                    f"${product.price}\n"

                )

            file.write("\n")

            file.write(

                f"Products: {summary['products']}\n"

            )

            file.write(

                f"Items: {summary['items']}\n"

            )

            file.write(

                f"Value: ${summary['value']}\n"

            )
