import factory_A

def main():
    myfactoryA = factory_A.Factory_A()

    print("product A:", myfactoryA.process_product("A"))
    print("product B:", myfactoryA.process_product("B"))

main()