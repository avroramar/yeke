class Summary:

    def build(

        self,

        products,

        manager

    ):

        return {

            "products": len(products),

            "items": manager.total_items(products),

            "value": manager.total_value(products)

        }
