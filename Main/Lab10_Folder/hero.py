#HERO CLASS : Inherrited from abtract class Entity
import check_input
from entity import Entity
from map import Map
import random

class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, max_hp = 25)
        self._row = 0
        self._col = 0
        self._loc = [self._row,self._col] #[Y,X]

    @property
    def location(self):
        return self._loc

    def attack(self,entity):
        dmg = random.randint(2, 5)
        Entity.take_damage(entity, dmg)

        print(f"you attack a {entity.name} for {dmg} damage.")

    def go_north(self): #MOVE UP
        m = Map()

        if self.location[0] - 1 >= 0: #change the condition
            self.location[0] -= 1
            return m[self.location[0]][self.location[1]]
        else:
            ''' You cant go that way'''''
            return 'o'

    def go_east(self): #MOVE RIGHT
        m = Map()
        if self.location[1] + 1 <= len(m[self._row])-1:

            self.location[1] += 1
            return m[self.location[0]][self.location[1]]
        else:

            return 'o'

    def go_south(self): #MOVE DOWN
        m = Map()
        if self.location[0] + 1 <= len(m[1]) -1:
            self.location[0] += 1
            return m[self.location[0]][self.location[1]]
        else:
            ''' You cant go that way'''''
            return 'o'

    def go_west(self): #MOVE LEFT
        m = Map()
        if self.location[1] - 1 >= 0:
            #self._row -= 1
            self.location[1] -= 1
            return m[self.location[0]][self.location[1]]
        else:

            ''' You cant go that way'''''
            return 'o'


