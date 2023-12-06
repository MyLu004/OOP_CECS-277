import random
from entity import Entity

class EasyZombie(Entity):
    def __init__(self):
        max_hp = random.randint(4,5)
        super().__init__("Easy Zombie",max_hp)

    def attack(self,entity):
        dmg = random.randint(1,5)
        Entity.take_damage(entity, dmg)
        print(f"{self.name} attack a {entity.name} for {dmg} damage.")