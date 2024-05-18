class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed: int = SLOW, radius: float = 5, color: str = "blue", on: bool = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        try:
            if 1 <= speed <= 3:
                self.__speed = speed
            else:
                raise ValueError("Invalid speed.")
        except ValueError as e:
            print(e)
        
    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        try:
            if radius > 0:
                self.__radius = radius
            else:
                raise ValueError("Invalid radius.")
        except ValueError as e:
            print(e)
        
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color

    def get_on(self):
        return self.__on
    
    def set_on(self, on):
        self.__on = on