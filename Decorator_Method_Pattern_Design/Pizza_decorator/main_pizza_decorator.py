import pizzasmall
import pizzalarge
import pepperoni
import mushroom

def main():
    myPizza = pizzasmall.PizzaSmall()
    myPizza = mushroom.Mushroom(myPizza)
    myPizza = pepperoni.Pepperoni(myPizza)

    myPizza2 = pizzalarge.PizzaLarge()
    myPizza2 = mushroom.Mushroom(myPizza2)

    print("total is: ",myPizza.get_price(), " dollars")
    print("my pizza is: ", myPizza.get_description())

    print("total is: ", myPizza2.get_price(), " dollars")
    print("my pizza is: ", myPizza2.get_description())

main()