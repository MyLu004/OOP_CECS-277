#ENEMY CLASS
import random
import check_input
from entity import Entity


class Enemy(Entity):
    def __init__(self):
        myEnemyList = ['Goblin','Vampire','Ghoul','Skeleton','Zombie']
        self._name = random.choice(myEnemyList)
        self._max_hp = random.randint(4,8)
        self._hp = self._max_hp

    def attack(self,entity):
        dmg = random.randint(1,4)
        Entity.take_damage(entity, dmg)
        print(f"{self.name} attack a {entity.name} for {dmg} damage.")
