import random
import enemy_factory
import zombie
import skeleton
import goblin

class ExpFactory(enemy_factory.EnemyFactory):
    def create_random(self):
        random_enemy = random.randint(1,3)

        if random_enemy == 1:
            return zombie.Zombie()
        elif random_enemy == 2:
            return skeleton.Skeleton()
        elif random_enemy == 3:
            return goblin.Goblin()