from sample_data import PRODUCTS
from inventory.models import Product

class Storage:

    def load(self):

        return [

            Product(**item)

            for item in PRODUCTS

        ]
