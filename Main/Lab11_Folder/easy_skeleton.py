import random
from entity import Entity

class EasySkeleton(Entity):
    def __init__(self):
        max_hp = random.randint(3,4)
        super().__init__("Easy Skeleton",max_hp)

    def attack(self,entity):
        dmg = random.randint(1,4)
        Entity.take_damage(entity, dmg)
        print(f"{self.name} attack a {entity.name} for {dmg} damage.")