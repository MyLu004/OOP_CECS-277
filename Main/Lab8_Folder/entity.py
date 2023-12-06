import abc
#class entity [abstract class]

class Entity(abc.ABC):
    def __init__(self,name = 'None',max_hp = 0):
        self._name = name
        self._max_hp = max_hp #fixed value
        self._hp = max_hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    def take_damage(self,dmg):
        #self.damage = dmg
        '''
        hp_entity - dmg
        '''
        # print('entity_hp: ',self._hp)
        # print('dmg: ',dmg)
        self._hp -= dmg
        if self.hp < 0:
            self._hp = 0

    def __str__(self):
        '''
        :return: Name: hp/max_hp
        '''
        return (f'{self._name}: {self._hp}/{self._max_hp}')

    @abc.abstractmethod
    def basic_attack(self,other):
        '''
        abstract class [basic attack]
        '''
        pass

    @abc.abstractmethod
    def special_attack(self,other):
        '''
        abstract class [special attack]
        '''
        pass
