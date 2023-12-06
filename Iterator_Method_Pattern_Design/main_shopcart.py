import shopping_cart
from item import Item
def main():
    myCart = shopping_cart.ShoppingCart()
    option = 0

    while option != 4:
        print('1. Add item to cart \n'
              '2. Display item \n'
              '3.Calculate total \n'
              '4.Quit')
        option = int(input("Please enter option: "))

        if option == 1:
            itemName = str(input("Please enter item name: "))
            price = float(input("Please enter item's price"))
            grocery = Item(itemName,price)
            myCart.add_item(grocery)

        elif option == 2:
            for item in myCart:
                print(item)
        elif option == 3:
            myTotal = 0
            for item in myCart:
                #iterate through the list and add price
                myTotal += item.price
            print("Total: $",str(myTotal))

main()