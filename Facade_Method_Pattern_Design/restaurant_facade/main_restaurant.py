import restaurant_facade

def main():
    myres = restaurant_facade.RestaurantFacade()

    choice = ''
    while choice != "Q":
        print(myres.get_menu() + "Q. Complete Order")
        choice = input("Enter Choice: ")
        print()
        if choice == "1":
            myres.order_item("Hamburger")
        elif choice == "2":
            myres.order_item("Fries")
        elif choice == "3":
            myres.order_item("Drink")
        elif choice == "Q":
            tot = myres.calc_total()
            print("Your total is: $" + str(tot))
    print("\nThank you!\nHere's your order: \n" + str(myres.get_order()))


main()