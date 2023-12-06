from dragon import Dragon
import random

class FlyingDragon(Dragon):
    def __init__(self,name, max_hp, swoop):
        super().__init__(name,max_hp)
        self._swoop = swoop

    def special_attack(self,other):
        if self._swoop > 0:
            flyingdragonDamage = random.randrange(5,8)
            Dragon.take_damage(other,flyingdragonDamage)
            #print(f'**Flying_Dragon : {self.name} | flying attack | {other.name} | damage : {flyingdragonDamage}')
            print(f'{self.name} swoops at you for {flyingdragonDamage} damage!')
            self._swoop -= 1
        else:
            print(f'{self.name} tries to swoop down to hit you, but failed.')
            #print(f"No Damage dealt, remain swoop is 0 : {self._swoop}")

    def __str__(self):
        return super(FlyingDragon, self).__str__()+ f"\nSwoop remaining: {self._swoop}"

