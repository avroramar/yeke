from config import REPORT_FILE

from inventory.storage import Storage
from inventory.manager import InventoryManager
from inventory.validator import Validator

from reports.summary import Summary
from reports.exporter import Exporter

products = Storage().load()

validator = Validator()

products = [

    product

    for product in products

    if validator.valid(product)

]

manager = InventoryManager()

summary = Summary().build(

    products,

    manager

)

print("\nWarehouse Inventory\n")

for product in products:

    print(product.name)

    print(f"Quantity : {product.quantity}")

    print(f"Price    : ${product.price}")

    print()

print("---------------------")

print(f"Products : {summary['products']}")

print(f"Items    : {summary['items']}")

print(f"Value    : ${summary['value']}")

Exporter().save(

    products,

    summary,

    REPORT_FILE

)
