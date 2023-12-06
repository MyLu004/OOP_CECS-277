import random
from entity import Entity

class Skeleton(Entity):
    def __init__(self):
        max_hp = random.randint(6,10)
        super().__init__("Mage Skeleton",max_hp)

    def attack(self,entity):
        dmg = random.randint(6,10)
        Entity.take_damage(entity, dmg)
        print(f"{self.name} attack a {entity.name} for {dmg} damage.")