#Class Product B: concreate product class : for each type of prodcut that factory can make

import product

class Product_B(product.Product):
    def use_product(self):
        return "Using product B"
