import adapter1
import adapter2
def main():
    object1 = adapter1.Adapter()
    print("usable1: ",object1.usable_method())
    print("calculate1 : ",object1.calculate_method())


    object2 = adapter2.Adapter()
    print("usable2: ",object2.usable_method())
    print("calculate2 : ", object2.calculate_method())

main()