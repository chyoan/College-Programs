from beverage import Beverage

class Beer(Beverage):
    def __init__(self, volume, is_chilled, alcoholic_content):
        super().__init__("Beer", volume, is_chilled)
        self.__alcoholic_content = alcoholic_content

    def get_type(self):
        if self.__alcoholic_content * 100 < 3:
            return "Flavored"
        elif self.__alcoholic_content * 100 < 6:
            return "Regular"
        else:
            return "Strong"

    def __str__(self):
        return super().__str__() + f" ({self.__alcoholic_content*100:.1f}% alcoholic content)"

    def get_alcoholic_content(self):
        return self.__alcoholic_content