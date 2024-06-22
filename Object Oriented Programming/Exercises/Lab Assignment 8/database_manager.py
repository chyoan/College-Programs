# Create a file named database_manager.py which contains the following class:
# • A class called MovieHouseDatabaseManager which has a single attribute called database_file of type String and has the following function:
# o a constructor that has a parameter of type String called database_file.
# o a function named get_connection. 
# This function should allow the app to connect to the database using the 3 attributes. 
# This function should be used throughout the class to connect to the database.
# o a function named register_movie which has a parameter of title, genre andcost. 
# This function will save the values to the movie table in their corresponding columns. 
# If the student was saved successfully, this function should return true. Otherwise, return false.
# o a function named remove_movie which has a parametor of id. 
# This method will update the is_deleted column of the movie with the same id as the parameter to true.
# o a function named retrieve_movies which has a parameter of genres, which is a List of strings. 
# This function will retrieve all movies that has genres found in the genres parameter. 
# If the array is empty, this function will instead retrieve all movies. This will return a list of Movie.
# o a function named retrieve_rooms. This function will retrieve all rooms from the database. 
# This will return a list of Movie.
# o a function named retrieve_recor dwhich has a parameter of room_id. 
# This function will retrieve the latest record of that room that is not yet finished. 
# If there are no records found, this will return an emptyRecordobject. 
# This function will also retrieve all movies associated with that record.
# o a function named check_in which has a parameter of room_id and movies, which is a List of Movie objects. 
# This function will create a room_record for with the parameters as its values. 
# This will also create a room_movie_record for each movie in the movies list. 
# This function will return true if the record was successfully created. Otherwise, return false.
# o a function named check_out which has a parameter of id. 
# This function will update the is_finished column of the record with the same id as the parameter. 
# This function will return true if the record was successfully updated. Otherwise, return false.

import sqlite3
from classes import Movie, Room, Record

class MovieHouseDatabaseManager:
    def __init__(self, database_file):
        self.database_file = database_file

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.database_file)
            return conn
        except sqlite3.Error as e:
            print(f"An error occurred while connecting to the database: {e}")

    def register_movie(self, title, genre, cost):
        conn = self.get_connection()
        try:
            crsr = conn.cursor()
            crsr.execute("INSERT INTO movie (title, genre, cost) VALUES (?, ?, ?)", (title, genre, cost))
            conn.commit()
            return crsr.lastrowid
        except Exception as e:
            print(f"An error occured: {e}")
            return False
        finally:
            conn.close()

    def remove_movie(self, id):
        conn = self.get_connection()
        try:
            crsr = conn.cursor()
            crsr.execute("UPDATE movie SET is_deleted = 1 WHERE id = ?", (id,))
            conn.commit()
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            conn.close()

    def retrieve_movies(self, genres):
        conn = self.get_connection()
        try:
            crsr = conn.cursor()
            if genres:
                placeholders = ', '.join('?' for _ in genres)
                query = f"SELECT * FROM movie WHERE genre IN ({placeholders})"
                crsr.execute(query, genres)
            else:
                crsr.execute("SELECT * FROM movie")
            rows = crsr.fetchall()
            movies = [Movie(row[0], row[1], row[2], row[3]) for row in rows]
            return movies
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

    def retrieve_rooms(self):
        conn = self.get_connection()
        try:
            crsr = conn.cursor()
            crsr.execute("SELECT * FROM room")
            rows = crsr.fetchall()
            rooms = [Room(row[0], row[1]) for row in rows]
            return rooms
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            conn.close()

    def retrieve_record(self, room_id):
        conn = self.get_connection()
        try:
            crsr = conn.cursor()
            crsr.execute("SELECT * FROM room_record WHERE room_id = ? AND is_finished = 0", (room_id,))
            room_record = crsr.fetchone()
            if room_record:
                crsr.execute("SELECT movie.* FROM room_movie_record JOIN movie ON movie.id = room_movie_record.movie_id WHERE room_record_id = ?", (room_record[0],))
                movies = [Movie(movie_row[0], movie_row[1], movie_row[2], movie_row[3]) for movie_row in crsr.fetchall()]
                record = Record(room_record[0], room_record[1], room_record[2], movies)
                return record
            else:
                return Record(None, None, None, [])
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

    def check_in(self, room_id, movies):
        conn = self.get_connection()
        try:
            crsr = conn.cursor()
            crsr.execute("INSERT INTO room_record (room_id, total_cost) VALUES (?, ?)", (room_id, sum([movie.get_cost() for movie in movies])))
            record_id = crsr.lastrowid
            for movie in movies:
                crsr.execute("INSERT INTO room_movie_record (movie_id, room_record_id) VALUES (?, ?)", (movie.get_id(), record_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"An error occured: {e}")
            return False
        finally:
            conn.close()

    def check_out(self, id):
        conn = self.get_connection()
        try:
            crsr = conn.cursor()
            crsr.execute("UPDATE room_record SET is_finished = 1 WHERE id = ?", (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"An error occured: {e}")
            return False
        finally:
            conn.close()