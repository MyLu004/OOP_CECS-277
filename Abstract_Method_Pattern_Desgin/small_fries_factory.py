
import abstract_fractory
import smallregfries
import smallspicyfries

class SmallFriesFactory(abstract_fractory.AbstractFriesFactory):
    def make_regular(self):
        return smallregfries.SmallRegFries()

    def make_spicy(self):
        return smallspicyfries.SmallRegFries()