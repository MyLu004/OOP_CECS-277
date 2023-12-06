
import componentA
import decorationA
import componentB
import decorationB

def main():
    obj1 = componentA.ComponentA()
    obj1 = decorationA.DecorationA(obj1)
    '''
    obj1 override
    '''
    obj1 = decorationA.DecorationA(obj1)

    obj2 = componentB.ComponentB()
    obj2 = decorationB.DecorationB(obj2)
    obj2 = decorationA.DecorationA(obj2)

    print("my object 2: ",obj2.operation())


    #print("my Decoration A: ", obj1.operation())



main()