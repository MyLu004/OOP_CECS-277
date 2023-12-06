import random
from entity import Entity

class Goblin(Entity):
    def __init__(self):
        max_hp = random.randint(4,6)
        super().__init__("Giant Goblin",max_hp)

    def attack(self,entity):
        dmg = random.randint(2,5)
        Entity.take_damage(entity, dmg)
        print(f"{self.name} attack a {entity.name} for {dmg} damage.")