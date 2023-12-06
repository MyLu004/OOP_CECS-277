
class Cook:
    #do the des later

    def __init__(self):
        self._cookable_items = []

    def add_cookable(self, item):
        self._cookable_items.append(item)

    def make_item(self, item):
        self._cookable_items.remove(item)
        return "finish making a " + item.name

