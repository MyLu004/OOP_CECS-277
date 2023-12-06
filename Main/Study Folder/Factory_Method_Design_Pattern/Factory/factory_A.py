#concrete Factory Class : override a creation method that decides which products this factory can makes.
#Define what product can do

import factory
import product_A
import product_B

class Factory_A(factory.Factory):
    def create_product(self,type):
        if type == "A":
            return product_A.Product_A()
        if type == "B":
            return product_B.Product_B()
