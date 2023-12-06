from dragon import Dragon
import random

class FireDragon(Dragon):
    def __init__(self,name, max_hp,f_shot):
        super().__init__(name,max_hp)
        self._fireshot = f_shot
    
    
    def special_attack(self, other):
        if self._fireshot > 0:
            firedragobDamage = random.randrange(5,9)
            Dragon.take_damage(other,firedragobDamage)
            self._fireshot -= 1

            #print(f'**Fire_Dragon : {self.name} | fire attack | {other.name} | damage : {firedragobDamage}')
            print(f'{self.name} engulfs you in flames for {firedragobDamage} damage!')

        else:
            print(f"{self.name} tries to spit fire at you but is all out of fire shots.")
    
    def __str__(self):
        return super(FireDragon, self).__str__() + f"\nFireshots remaining: {self._fireshot}"

