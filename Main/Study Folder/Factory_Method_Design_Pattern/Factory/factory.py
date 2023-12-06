#Abstract base class factory : one or more types of factories can made

import abc

class Factory(abc.ABC):
    def process_product(self,type):
        prod = self.create_product(type)
        '''
        product_A.Product_A.use_prodcut()
        product_B.Product_B.use_prodcut()
        '''
        return prod.use_product()

    @abc.abstractmethod
    def create_product(self,type):
        pass