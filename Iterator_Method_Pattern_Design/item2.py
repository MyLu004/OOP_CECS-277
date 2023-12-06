
class Items:
    def __init__(self):
        self._items = [1,2,3,4,5]

    def __getitem__(self, item):
        return self._items[item]

if __name__ == "__main__":
    myItems = Items()
    for i in myItems:
        print(i)