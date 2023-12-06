import enemy_factory
import easy_zombie
import easy_skeleton
import easy_goblin
import random

class BegFactory(enemy_factory.EnemyFactory):
    def create_random(self):
        random_enemy = random.randint(1,3)

        if random_enemy == 1:
            return easy_zombie.EasyZombie()
        elif random_enemy == 2:
            return easy_skeleton.EasySkeleton()
        elif random_enemy == 3:
            return easy_goblin.EasyGoblin()