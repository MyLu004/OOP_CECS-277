import random
import check_input
from hero import Hero
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon


if __name__ == "__main__":

    heroName = str(input("What is your name, challenger? "))
    dragonName = 'Deadly Nadder'
    firedragonName = 'Gronckle'
    flyingdragonName = 'Timberjack'


    myHero = Hero(heroName,50) #name,hp
    myDragon = Dragon(dragonName,10) #name,hp
    myFireDragon = FireDragon(firedragonName,15,3) #name,hp,fireball
    myFlyingDragon = FlyingDragon(flyingdragonName,20,5) #name,hp,swomp

    DragonList = [myDragon,myFireDragon,myFlyingDragon] #DragonList [0,1,2]



    print(f"Welcome to dragon training, {heroName} \nYou must defeat {len(DragonList)} dragons.\n")

    while myHero.hp > 0 and len(DragonList) != 0:#conditon will be hp > 0 and the list is not empty

        print(myHero)
        for idx in range(len(DragonList)):
            print(f"{idx+1}.Attack {DragonList[idx]}")

        dragonTarget = (check_input.get_int_range("Choose a dragon to attack: ",1,len(DragonList)))-1


        print('\nAttack with: \n1. Sword (2 D6) \n2. Arrow (1 D12)')
        heroAttack = check_input.get_int_range("Enter Weapon: ",1,2)


        print()
        #Hero Attack
        if heroAttack == 1:
            myHero.basic_attack(DragonList[dragonTarget])
        elif heroAttack == 2:
            myHero.special_attack(DragonList[dragonTarget])

        #Dragon Attack
        if len(DragonList) > 1:
            rand_choice= [value for value in range(0,len(DragonList)) if value != dragonTarget]
            dragonRandom = random.choice(rand_choice) #determind the dragon will attack u
            dragonRandomAttack = random.randrange(1,3)  # 1.basic | other#.special
            #determind which attack will hit


            if dragonRandomAttack == 1:
                """Dragon Basic Attack"""
                DragonList[dragonRandom].basic_attack(myHero)
            else:
                """Dragon Special Attack"""
                DragonList[dragonRandom].special_attack(myHero)


        #Check Dragon HP to remove [after the attack]
        for value in range(len(DragonList)):
            if DragonList[value].hp == 0:
                #print(f'{DragonList[value].name} died')
                DragonList.pop(value)
                break

        print()

    if myHero.hp <= 0:
        print("-----------------------------------------------------------------------------")
        print('You have been defeated. GAME OVER')

    elif len(DragonList) == 0:
        print("-----------------------------------------------------------------------------")
        print("Congratulations! You have defeated all 3 dragons, you have passed the trial")

    print("---END OF THE GAME---")






