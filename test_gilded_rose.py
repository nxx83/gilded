# -*- coding: utf-8 -*-
import unittest
from approvaltests import approvals, combination_approvals
from gilded_rose import GildedRose
from items import ProductsFactory

products = ProductsFactory()


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [products.create_item("foo", sell_in=1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("foo", items[0].name)



    def test_conjured_before_sell_date(self):
        items = [products.create_item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_conjured_on_sell_date(self):
        items = [products.create_item(name="Conjured Mana Cake", sell_in=0, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_conjured_after_sell_date(self):
        items = [products.create_item(name="Conjured Mana Cake", sell_in=-2, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)




if __name__ == '__main__':
    unittest.main()
