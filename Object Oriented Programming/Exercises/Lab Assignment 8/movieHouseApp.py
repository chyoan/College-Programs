# Tkinter Application with DB Activity
# Create a Moviehouseapp that allows the user to register a customer and reserve a room for them. 
# 
# For this app, create a database with 4 tables:
# • a table named roomw hich contains the following columns:
# - id (Primary Key)
# - cost
# 
# NOTE: Manually enter 4 data into this table. The cost can be any amount.
# • a table named movie which contains the following columns:
# - id (Primary Key)
# - title of type VARCHAR
# - genre of type VARCHAR
# - is_deleted of type TINYINT, INTEGER, or BOOLEAN with default value set to 0.
# - cost of type real or double
# • a table named room_record which contains the following columns:
# - id (Primary Key)oroom_id (Foreign Key)
# - total_cost of type real or double
# - is_finished of type TINYINT, INTEGER, or BOOLEAN with default value set to 0.
# • a table named room_movie_record which contains the following columns:
# - id (Primary Key)
# - movie_id (Foreign Key)
# - room_record_id (Foreign Key)

import sqlite3

conn = sqlite3.connect("moviehouse.db")
crsr = conn.cursor()

crsr.execute("""CREATE TABLE IF NOT EXISTS room (
             id INTEGER PRIMARY KEY, 
             cost REAL)""")

crsr.execute("""CREATE TABLE IF NOT EXISTS movie (
             id INTEGER PRIMARY KEY, 
             title VARCHAR(255), 
             genre VARCHAR(255), 
             is_deleted INTEGER DEFAULT 0, 
             cost REAL)""")

crsr.execute("""CREATE TABLE IF NOT EXISTS room_record (
             id INTEGER PRIMARY KEY, 
             room_id INTEGER, 
             total_cost REAL, 
             is_finished INTEGER DEFAULT 0,
             FOREIGN KEY(room_id) REFERENCES room(id))""")

crsr.execute("""CREATE TABLE IF NOT EXISTS room_movie_record (
             id INTEGER PRIMARY KEY, 
             movie_id INTEGER, 
             room_record_id INTEGER,
             FOREIGN KEY(movie_id) REFERENCES movie(id),
             FOREIGN KEY(room_record_id) REFERENCES room_record(id))""")

conn.commit()
conn.close()