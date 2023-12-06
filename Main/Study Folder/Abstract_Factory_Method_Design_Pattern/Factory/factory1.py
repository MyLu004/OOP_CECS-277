import abstract_factory
import producta1
import productb1

class Factory1(abstract_factory.AbstractFactory):
    def create_prod_a(self):
        return producta1.ProductA1()

    def create_prod_b(self):
        return productb1.ProductB1()