import abstract_fractory
import largespicyfries

class LargeFriesFactory(abstract_fractory.AbstractFriesFactory):
    def make_regular(self):
        return la()

    def make_spicy(self):
        return largespicyfries.LargeSpicyFries()