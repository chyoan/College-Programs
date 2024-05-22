# School Library - Python
# by CodeChum Admin
# 
# Implement the class Book with the following details:
# Class - Book:
# Private Properties:
# title (type: str): Represents the title of the book.
# number_of_pages (type: int): Holds the number of pages in the book.
# is_fictional (type: bool): Indicates whether the book is fictional.
# Getters and setters:
# get_title(self) -> str and set_title(self, title: str) - for retrieving and setting the title property
# get_number_of_pages(self) -> int and set_number_of_pages(self, pages: int) - for retrieving and setting the number_of_pages property
# get_is_fictional(self) -> bool and set_is_fictional(self, is_fictional: bool) - for retrieving and setting the is_fictional property

class Book:
    def __init__(self):
        self.__title = ""
        self.__number_of_pages = ""
        self.__is_fictional = ""

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, pages):
        self.__number_of_pages = pages

    def get_is_fictional(self):
        return self.__is_fictional

    def set_is_fictional(self, is_fictional):
        self.__is_fictional = is_fictional