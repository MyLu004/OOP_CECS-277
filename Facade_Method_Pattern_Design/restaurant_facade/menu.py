import item

class Menu:
    """represent the list of the menu at a restaurant"""
    #do the attribute
    def __init__(self):
        self._menu = []
        #create the menu file later
        file = open("menuitem.txt")
        for i in file:
            vals = i.strip().split(",")
            self._menu.append(item.Item(vals[0],int(vals[1]),vals[2]=="True"))

    def __getitem__(self, item):
        return self._menu[item]
    def __len__(self):
        return len(self._menu)

    def get_item_by_name(self, item_name):
        for i in self._menu:
            if item_name == i.name:
                return i