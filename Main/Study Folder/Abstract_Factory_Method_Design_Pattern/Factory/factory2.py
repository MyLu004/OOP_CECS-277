import abstract_factory
import producta2
import productb2


class Factory2(abstract_factory.AbstractFactory):
    def create_prod_a(self):
        return producta2.ProductA2()

    def create_prod_b(self):
        return productb2.ProductB2()