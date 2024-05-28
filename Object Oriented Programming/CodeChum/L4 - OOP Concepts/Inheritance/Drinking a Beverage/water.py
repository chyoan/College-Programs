from beverage import Beverage

class Water(Beverage):
    def __init__(self, volume, is_chilled, type='Regular'):
        super().__init__("Water", volume, is_chilled)
        self.__type = type
        
    def get_type(self):
        return self.__type