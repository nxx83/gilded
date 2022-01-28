from store import Products
from items_list import AgedBrie, BackstagePasses, Conjured, Sulfuras, Item


class ProductsFactory:

    @staticmethod
    def create_item(name, sell_in, quality):

        if name == Products.AGED_BRIE.value:
            return AgedBrie(name, sell_in, quality)

        elif name == Products.BACKSTAGE_PASSES.value:
            return BackstagePasses(name, sell_in, quality)

        elif name == Products.CONJURED.value:
            return Conjured(name, sell_in, quality)

        elif name == Products.SULFURAS.value:
            return Sulfuras(name, sell_in, quality)

        else:
            return Item(name, sell_in, quality)


