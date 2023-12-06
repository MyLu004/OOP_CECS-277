import factory1
import factory2

def main():
    myfact1 = factory1.Factory1() #factory 1

    prod_a1 = myfact1.create_prod_a() #product A1
    print("Product A1: ",prod_a1.func_a())

    prod_b1 = myfact1.create_prod_b() #product B1
    print("Product B1: ", prod_b1.func_b())
#############################################################
    myfact2 = factory2.Factory2() #factory 2

    prod_a2 = myfact2.create_prod_a() #product A2
    print("Product A2: ",prod_a2.func_a())

    prod_b2 = myfact2.create_prod_b() #product B2
    print("Product B2: ",prod_b2.func_b())


main()