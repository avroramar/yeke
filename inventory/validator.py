class Validator:

    def valid(self, product):

        return (

            product.quantity >= 0

            and

            product.price >= 0

        )
