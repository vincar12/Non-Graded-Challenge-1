import unittest

from Muhammad_Vincar_Rafi_Theoseta_app import ShoppingCart
from Muhammad_Vincar_Rafi_Theoseta_app import CartItem

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.item1 = CartItem("Sate", "30000")

    def test_addcart(self):
        shop = ShoppingCart()
        shop.addcart(self.item1)
        self.assertEqual(len(shop.shopcart), 1)

    def test_removecart(self):
        shop = ShoppingCart()
        shop.addcart(self.item1)
        shop.removecart(0) #no index barang dalam list
        self.assertEqual(len(shop.shopcart), 0)

    def test_showcart(self):
        shop = ShoppingCart()
        shop.addcart(self.item1)
        shop.showcart()
        self.assertEqual(shop.showcart, "no|nama|harga\n1|Sate|30000")


unittest.main(argv=[''], verbosity=2, exit=False)