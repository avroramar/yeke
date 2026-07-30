import unittest

from inventory.manager import InventoryManager


class InventoryManagerTests(unittest.TestCase):

    def test_create_manager(self):

        manager = InventoryManager()

        self.assertIsNotNone(manager)

    def test_empty_inventory(self):

        manager = InventoryManager()

        self.assertEqual(

            len(manager.products),

            0

        )


if __name__ == "__main__":

    unittest.main()
