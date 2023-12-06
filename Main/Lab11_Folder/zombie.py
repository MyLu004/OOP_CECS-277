import random
from entity import Entity

class Zombie(Entity):
    def __init__(self):
        max_hp = random.randint(8,10)
        super().__init__("Fast Zombie",max_hp)

    def attack(self,entity):
        dmg = random.randint(5,12)
        Entity.take_damage(entity, dmg)
        print(f"{self.name} attack a {entity.name} for {dmg} damage.")