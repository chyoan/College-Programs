# Lastly, create the main.py which should contain the following classes:
# • A class called RecordWindow which inherits from the Tkinter Window class and contains the following attributes:
# o room -a Room object 
# o db_manager -a MovieHouseDatabaseManager object
# o record -a Record object 
# 
# This class should also contain the following components:
# • 2 listboxes named movies_list and movies_to_view_list
# • 4 buttons with the following functionality:
# o add_movie_button will add movies to movies_to_view_list
# o remove_movie_button will remove movies from movies_to_view_list
# o check_in_button will create a record for the room with its movies being the movies in movies_to_view_listy calling the check_in function of MovieHouseDatabaseManager
# o check_out_button will checkout the record of this class by calling the check_out function of MovieHouseDatabaseManager class.
# • a label named total_cost_label which will display the total cost of the room + movies to view.
# This class should have a constructor that has a parameter for each attributes and implement the following behaviors:
# • check_out_button should be disabled and check_in_button should be enabled if there are no records. 
# Otherwise, check_out_button should be disabled and check_in_button should be enabled.
# • A class named MovieHouseWindow which inherits from the Tkinter window class. 
# This class should have a single attribute named _database_manager which is of type MovieHouseDatabaseManager. 
# The class' constructor should have a parameter of database_file_name and initializes the_database_manager with the parameter.
#
# o 5 checkboxes used for filtering movies_list that has the following details:
# ▪ a checkbox named adventure_checkbutton and labeled "Adventure".
# ▪ a checkbox named comedy_checkbutton and labeled "Comedy".
# ▪ a checkbox named fantasy_checkbutton and labeled "Fantasy".
# ▪ a checkbox named romance_checkbutton and labeled "Romance".
# ▪ a checkbox named tragedy_checkbutton and labeled "Tragedy".
# 
# o 4 buttons named room1_button, room2_button, room3_button, and room4_button. 
# When a button is clicked, retrieve the corresponding record on a room and then show the RecordWindow.
# o a listbox named movies_list which will display the movies retrieved from the database
# o 3 entries named movie_title_entry, cost_entry, and genre_entry.
# o 2 buttons that do the following:
# ▪ add_button which will add the movie to the database with its title, cost, and genre being the values of their respective components.
# ▪ delete_button which will delete the movie from the database that has the same id as the movie selected from the list.
#
# This class should also contain the following components:
# Both of these buttons will cause movies_list to refetch data from the database.
# The app should have this general flow:
# • View all movies in the database and add filters accordingly.
# • Should be able to add and delete movies in the app.
# • Should be able to display all buttons for theRooms(4)
# • Should be able to check in a customer by clicking a room which will display the record window.
# • Should be able to check out a customer by clicking a room which will display the record window.
#
# In addition, these following conditions should be followed:
# • The app should retrieve all room and all movies data on app start. Then populate the necessary components of applicable.
# • The RecordWindow should close on check in and check out.

from tkinter import *
from classes import Movie, Room, Record
from database_manager import MovieHouseDatabaseManager

class RecordWindow(Tk):
    def __init__(self, room, db_manager, record):
        super().__init__()
        self.room = room
        self.db_manager = db_manager
        self.record = record
        
        self.title(f"Room 1")
        self.geometry("800x500")

        self.frameU = Frame(self)
        self.frameU.pack(side=TOP, fill=BOTH, expand=1, padx=20, pady=20)
        
        self.frameD = Frame(self)
        self.frameD.pack(side=BOTTOM, fill=BOTH, expand=1, padx=20, pady=20)
        
        self.frameLeft = Frame(self.frameU)
        self.frameLeft.pack(side=LEFT, fill=BOTH, expand=1, padx=10, pady=10)
        
        self.frameRight = Frame(self.frameU)
        self.frameRight.pack(side=LEFT, fill=BOTH, expand=1, padx=10, pady=10)

        self.moviesL = Label(self.frameLeft, text="Movies")
        self.moviesL.pack(pady=(5,0))
        
        self.movies_list = Listbox(self.frameLeft)
        self.movies_list.pack(fill=BOTH, expand=1)

        self.movies_listL = Label(self.frameRight, text="Movies to watch")
        self.movies_listL.pack(pady=(5,0))
        
        self.movies_to_view_list = Listbox(self.frameRight)
        self.movies_to_view_list.pack(fill=BOTH, expand=1)
        
        self.add_movie_button = Button(self.frameLeft, text="Add Movie", command=self.add_movie)
        self.add_movie_button.pack(side=BOTTOM, pady=10)
        
        self.remove_movie_button = Button(self.frameRight, text="Remove Movie", command=self.remove_movie)
        self.remove_movie_button.pack(side=BOTTOM, pady=10)

        self.frameTotalCost = Frame(self.frameD)
        self.frameTotalCost.pack(fill=X)
        
        self.total_cost_label = Label(self.frameTotalCost, text="Total Cost: $0.00")
        self.total_cost_label.pack(pady=10)
        
        self.frameButtonsD = Frame(self.frameD)
        self.frameButtonsD.pack(side=BOTTOM, pady=(0, 10))
        
        self.check_in_button = Button(self.frameButtonsD, text="Check In", command=self.check_in)
        self.check_in_button.pack(side=LEFT, padx=5)
        
        self.check_out_button = Button(self.frameButtonsD, text="Check Out", command=self.check_out)
        self.check_out_button.pack(side=LEFT, padx=5)

    def add_movie(self):
        selected_movie = self.movies_list.get(self.movies_list.curselection())
        self.movies_to_view_list.insert(END, selected_movie)

    def remove_movie(self):
        selected_movie = self.movies_to_view_list.get(self.movies_to_view_list.curselection())
        self.movies_to_view_list.delete(ANCHOR)

    def check_in(self):
        movies_to_view = self.movies_to_view_list.get(0, END)
        self.record = Record(self.room.get_id(), movies_to_view)
        self.db_manager.check_in(self.record)
        self.check_in_button.config(state=DISABLED)
        self.check_out_button.config(state=NORMAL)

    def check_out(self):
        self.db_manager.check_out(self.record)
        self.check_in_button.config(state=NORMAL)
        self.check_out_button.config(state=DISABLED)
        self.movies_to_view_list.delete(0, END)
        self.total_cost_label.config(text=f"Total Cost: {self.record.get_total_cost()}")

class MovieHouseWindow(Tk):
    def __init__(self, database_file_name):
        super().__init__()
        self._database_manager = MovieHouseDatabaseManager(database_file_name)
        
        self.title("Movie House")
        self.geometry("800x500")
        
        self.leftF = Frame(self)
        self.leftF.pack(side=LEFT, fill=BOTH, expand=1, padx=20, pady=20)
        
        self.registerF = Frame(self.leftF, relief=RIDGE, borderwidth=1)
        self.registerF.pack(side=TOP, fill=BOTH, expand=1, pady=(0, 20))
        
        self.moviesF = Frame(self.leftF, relief=RIDGE, borderwidth=1)
        self.moviesF.pack(side=BOTTOM, fill=BOTH, expand=1)
        
        self.roomsF = Frame(self, relief=RIDGE, borderwidth=1)
        self.roomsF.pack(side=RIGHT, fill=BOTH, expand=1, padx=20, pady=20)
        
        self.movieL = Label(self.moviesF, text="Movies")
        self.movieL.pack(pady=(5,0))

        self.checkboxes_frame = Frame(self.moviesF)
        self.checkboxes_frame.pack(side=RIGHT, padx=(0, 50), pady=(0, 50))

        self.movielist_frame = Frame(self.moviesF)
        self.movielist_frame.pack(side=LEFT)

        self.genreL = Label(self.checkboxes_frame, text="Genres")
        self.genreL.pack()
        
        self.adventure_checkbutton = Checkbutton(self.checkboxes_frame, text="Adventure")
        self.adventure_checkbutton.pack(anchor='w')
        
        self.comedy_checkbutton = Checkbutton(self.checkboxes_frame, text="Comedy")
        self.comedy_checkbutton.pack(anchor='w')
        
        self.fantasy_checkbutton = Checkbutton(self.checkboxes_frame, text="Fantasy")
        self.fantasy_checkbutton.pack(anchor='w')
        
        self.romance_checkbutton = Checkbutton(self.checkboxes_frame, text="Romance")
        self.romance_checkbutton.pack(anchor='w')
        
        self.tragedy_checkbutton = Checkbutton(self.checkboxes_frame, text="Tragedy")
        self.tragedy_checkbutton.pack(anchor='w')
        
        self.roomL = Label(self.roomsF, text="Rooms")
        self.roomL.pack(pady=(5,0))

        self.room1_button = Button(self.roomsF, text="Room 1", command=self.room1_button, height=5, width=30)
        self.room1_button.pack(padx=10, pady=10)
        
        self.room2_button = Button(self.roomsF, text="Room 2", command=self.room2_button, height=5, width=30)
        self.room2_button.pack(padx=10, pady=10)
        
        self.room3_button = Button(self.roomsF, text="Room 3", command=self.room3_button, height=5, width=30)
        self.room3_button.pack(padx=10, pady=10)
        
        self.room4_button = Button(self.roomsF, text="Room 4", command=self.room4_button, height=5, width=30)
        self.room4_button.pack(padx=10, pady=10)

        self.movies_list = Listbox(self.movielist_frame, selectmode=SINGLE, height=10, width=30)
        self.movies_list.pack(anchor='e', padx=20, pady=5)

        self.registerL = Label(self.registerF, text="Register")
        self.registerL.pack(pady=(5,0))

        self.title_frame = Frame(self.registerF)
        self.title_frame.pack(side=TOP, padx=5, pady=5)
        self.movie_title_label = Label(self.title_frame, text="Title:", width=10)
        self.movie_title_label.pack(side=LEFT)
        self.movie_title_entry = Entry(self.title_frame)
        self.movie_title_entry.pack(side=LEFT)
        
        self.cost_frame = Frame(self.registerF)
        self.cost_frame.pack(side=TOP, padx=5, pady=5)
        self.cost_label = Label(self.cost_frame, text="Cost:", width=10)
        self.cost_label.pack(side=LEFT)
        self.cost_entry = Entry(self.cost_frame)
        self.cost_entry.pack(side=LEFT)
        
        self.genre_frame = Frame(self.registerF)
        self.genre_frame.pack(side=TOP, padx=5, pady=5)
        self.genre_label = Label(self.genre_frame, text="Genre:", width=10)
        self.genre_label.pack(side=LEFT)
        self.genre_entry = Entry(self.genre_frame)
        self.genre_entry.pack(side=LEFT)

        self.add_button = Button(self.registerF, text="Add Movie", command=self.add_button)
        self.add_button.pack(side=BOTTOM, anchor='e', padx=5, pady=5)

        self.delete_button = Button(self.movielist_frame, text="Remove Movie", command=self.delete_button)
        self.delete_button.pack(side=BOTTOM, anchor='w', padx=60, pady=5)

    def room1_button(self):
        room = self._database_manager.retrieve_rooms()
        record_window = RecordWindow(room, self._database_manager, None)
        record_window.mainloop()

    def room2_button(self):
        room = self._database_manager.retrieve_rooms()
        record_window = RecordWindow(room, self._database_manager, None)
        record_window.mainloop()

    def room3_button(self):
        room = self._database_manager.retrieve_rooms()
        record_window = RecordWindow(room, self._database_manager, None)
        record_window.mainloop()

    def room4_button(self):
        room = self._database_manager.retrieve_rooms()
        record_window = RecordWindow(room, self._database_manager, None)
        record_window.mainloop()

    def add_button(self):
        title = self.movie_title_entry.get()
        cost = self.cost_entry.get()
        genre = self.genre_entry.get()
        movie_id = self._database_manager.register_movie(title, genre, cost)
        movie = Movie(movie_id, title, genre, cost)
        self.movies_list.insert(END, movie)

    def delete_button(self):
        selected_index = self.movies_list.curselection()[0]
        selected_item = self.movies_list.get(selected_index)
        movie_id = selected_item.split(" - ")[0]
        self._database_manager.remove_movie(int(movie_id))
        self.movies_list.delete(selected_index)

if __name__ == "__main__":
    root = MovieHouseWindow("moviehouse.db")
    root.mainloop()