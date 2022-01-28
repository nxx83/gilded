class GildedRose(object):
    """
    Used to update items properties.
    """

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()
