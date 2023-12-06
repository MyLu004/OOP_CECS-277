
import hero
import beg_factory
import exp_factory
import map
if __name__ == "__main__":
    myHero = hero.Hero("Kinoko")

    myMap = map.Map()
    myMap.load_map(1)

    myMap.reveal(myHero.location)
    myHero.go_south()

    myMap.reveal(myHero.location)
    myHero.go_south()

    myMap.reveal(myHero.location)
    myHero.go_south()

    myMap.reveal(myHero.location)
    myHero.go_east()

    myMap.reveal(myHero.location)
    myHero.go_east()

    myMap.reveal(myHero.location)
    myHero.go_south()

    myMap.reveal(myHero.location)
    myHero.go_east()

    myMap.load_map(2)

    myMap.reveal(myHero.location)
    myHero.go_west()

    print(myMap.show_map(myHero.location))
