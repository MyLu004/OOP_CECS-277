import random
from entity import Entity


#print(self.__str__()) #print Name : hp/max_hp
class Hero(Entity):
    def basic_attack(self,other):
        Damran1 = random.randrange(1,6)
        Damran2 = random.randrange(1,6)
        heroDamageBasic = Damran1 + Damran2
        Entity.take_damage(other,heroDamageBasic)

        #print(f'Hero : {self.name} | basic attack | {other.name} | damage: {heroDamageBasic}')
        print(f'{self.name} slashes the {other.name} with their sword for {heroDamageBasic} damage!')

    def special_attack(self,other):
        heroDamageSpc = random.randrange(1,12)
        Entity.take_damage(other, heroDamageSpc)

        #print(f'*Hero : {self.name} | special attack | {other.name} | damage: {heroDamageSpc}')
        print(f'{self.name} hits the {other.name} with an arrow for {heroDamageSpc} damage!')



# if __name__ == "__main__":
#     myHero = Hero('Kinoko')
#     myHero.take_damage(25)
#     myHero.basic_attack('Dragon')