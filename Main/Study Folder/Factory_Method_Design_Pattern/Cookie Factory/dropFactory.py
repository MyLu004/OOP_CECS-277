import cookieFactory
import drop_c_chip
import drop_PB

class DropFactory(cookieFactory.CookieFactory):
    def make_cookie(self,type):
        if type == "CC":
            return drop_c_chip.DropCChip()
        if type == "PB":
            return drop_PB.DropPB()