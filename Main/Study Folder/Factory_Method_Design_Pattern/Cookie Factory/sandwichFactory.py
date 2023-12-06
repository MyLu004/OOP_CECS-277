import cookieFactory
import sandwichOreo
import sandwichTea

class SandwichFactory(cookieFactory.CookieFactory):
    def make_cookie(self,type):
        if type == "OR":
            return sandwichOreo.SandWichOreo()
        if type == "TE":
            return sandwichTea.SandwichTea()