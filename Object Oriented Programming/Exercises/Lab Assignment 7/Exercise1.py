# Import the Tkinter package
from tkinter import *

# This method is called when the button is pressed
def clicked():
    print("The button has been clicked!")

# Create the main window
root = Tk()
# Set the window title
root.title("A First GUI Program")
# Set the window size
root.geometry('300x300')

# Create a button with the text "Click this button!" that calls the clicked method when pressed
button1 = Button(root, text="Click this button!", command=clicked)

# Make the button visible at the bottom of the frame 
button1.pack(side='bottom')

# Start the application running
root.mainloop()