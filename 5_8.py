import random

class BingoCage:
    def __init__(self, items):
        self._item = list(items)
        random.shuffle(self._item)

    def pick(self):
        try:
            return self._item.pop()
        except IndexError:
            raise LookupError('pick from empty BingpCage')

    def __ceil__(self):
        return self.pick()