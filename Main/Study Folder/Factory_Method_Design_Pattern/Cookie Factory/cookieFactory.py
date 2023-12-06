import abc

class CookieFactory(abc.ABC):
    def process_cookie(self,type):
        cookie = self.make_cookie(type)
        return cookie.eat_cookie()

    @abc.abstractmethod
    def make_cookie(self,type):
        pass