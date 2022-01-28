
MIN_QUALITY = 0
MAX_QUALITY = 50
EPIC_MAX_QUALITY = 80
MIN_SELL_IN_VALUE = 0




class Item:

    def __init__(self, name, sell_in, quality):

        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update(self) -> None:

        self._update_sell_in()
        self.quality = self._update_quality(self.sell_in)

    def _update_quality(self, sell_in: int) -> int:

        if sell_in >= 0:
            return max(self.quality - 1, MIN_QUALITY)
        else:
            return max(self.quality - 2, MIN_QUALITY)

    def _update_sell_in(self):

        self.sell_in -= 1


class AgedBrie(Item):

    def _update_quality(self, sell_in: int) -> int:
        if self.quality < 0:
            return MIN_QUALITY

        if sell_in >= 0 and self.quality > 0:
            return min(self.quality + 1, MAX_QUALITY)
        else:
            return min(self.quality + 2, MAX_QUALITY)


class BackstagePasses(Item):

    def _update_quality(self, sell_in: int) -> int:
        if sell_in > 10:
            return min(self.quality + 1, MAX_QUALITY)
        elif sell_in > 5:
            return min(self.quality + 2, MAX_QUALITY)
        elif sell_in >= 0:
            return min(self.quality + 3, MAX_QUALITY)
        else:
            return MIN_QUALITY


class Conjured(Item):

    def _update_quality(self, sell_in: int) -> int:
        if self.quality < 0:
            return MIN_QUALITY


        if sell_in >= 0:
            return max(self.quality - 2, MIN_QUALITY)
        else:
            return max(self.quality - 4, MIN_QUALITY)


class Sulfuras(Item):

    def _update_quality(self, sell_in: int):
        if self.quality > EPIC_MAX_QUALITY:
            return EPIC_MAX_QUALITY
        else:
            return EPIC_MAX_QUALITY

    def _update_sell_in(self):
        pass
