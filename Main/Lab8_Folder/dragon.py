import random
from entity import Entity

class  Dragon(Entity):
    def basic_attack(self,other):
        dragonDamageBasic = random.randrange(3,7)
        Entity.take_damage(other,dragonDamageBasic)


        #print(f'Dragon :  {self.name} | basic attack | {other.name} | damage : {dragonDamageBasic}')
        print(f'{self.name} smashes you with its tail for {dragonDamageBasic} damage!')

    def special_attack(self,other):
        dragonDamageSpc = random.randrange(4,8)
        Entity.take_damage(other, dragonDamageSpc)

        #print(f'Dragon : {self.name} | special attack | {other.name} | damage : {dragonDamageSpc}')
        print(f'{self.name} slashes you with its claws for {dragonDamageSpc} damage!')
