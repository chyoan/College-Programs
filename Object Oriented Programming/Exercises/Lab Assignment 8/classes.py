# Create a file named classes.py which contains the following classes:
# • A class called Movie which contains the following attributes:
# - id 
# - title
# - genre
# - cost

# This class should also contain a constructor that contains a parameter for each attributes. 
# It should also contain getters and setters. 
# This class should also override the __str__ function to display the movie's id and title, separated by a dash, just like in the example below.
# 1 -The Movie
# 
# • A class called Room which contains the following attributes:
# - id 
# - cost
# • A class called Record which contains the following attributes:
# - id
# - room_id 
# - total_cost 
# - movies -a list of Movie
# 
# Both Room and Record classes should contain a constructor that contains a parameter for each attributes. They should also contain getters and setters

class Movie:
    def __init__(self, id, title, genre, cost):
        self.__id = id
        self.__title = title
        self.__genre = genre
        self.__cost = cost

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
    
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
    
    def get_genre(self):
        return self.__genre
    
    def set_genre(self, genre):
        self.__genre = genre
    
    def get_cost(self):
        return self.__cost
    
    def set_cost(self, cost):
        self.__cost = cost

    def __str__(self):
        return f"{self.__id} - {self.__title}"


class Room:
    def __init__(self, id, cost):
        self.__id = id
        self.__cost = cost

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_cost(self):
        return self.__cost
    
    def set_cost(self, cost):
        self.__cost = cost
        
        
class Record:
    def __init__(self, id, room_id, total_cost, movies):
        self.__id = id
        self.__room_id = room_id
        self.__total_cost = total_cost
        self.__movies = movies

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_room_id(self):
        return self.__room_id
    
    def set_room_id(self, room_id):
        self.__room_id = room_id
    
    def get_total_cost(self):
        return self.__total_cost
    
    def set_total_cost(self, total_cost):
        self.__total_cost = total_cost

    def get_movies(self):
        return self.__movies

    def set_movies(self, movies):
        self.__movies = movies