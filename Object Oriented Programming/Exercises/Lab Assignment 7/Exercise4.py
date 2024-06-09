# Import all from tkinter
from tkinter import *

# Create main window'
root = Tk()
# Set window title
root.title("The Drawing Canvas and Events")
# Set window size
root.geometry('400x400')

# Create a canvas widget with blue background
canvas = Canvas(root, bg='blue')
# Pack the canvas to fill the available space in both directions
canvas.pack(expand=1, fill=BOTH)

# Initialize variables for shape drawing
shape = "s"
fillColor = None
color = "black"

# Function to switch to drawing squares
def sKey(event):
    global shape
    print("Lower case s key pressed: Now drawing squares")
    shape = "s"
    
# Function to switch to drawing circles
def cKey(event):
    global shape
    print("Lower case c key pressed: Now drawing circles")
    shape = "c"

# Function to switch to transparent fill mode
def fKey(event):
    global fillColor
    print("Lower case f key pressed: Now drawing transparent shapes")
    fillColor = None

# Function to switch to filled shape mode
def FKey(event):
    global fillColor
    print("Upper case F key pressed: Now drawing filled shapes")
    fillColor = color

# Function to change drawing color
def changeColor(new_color):
    global fillColor, color
    color = new_color
    if fillColor != None:
        fillColor = color

# Function to switch to drawing red shapes
def rKey(event):
    print("Lower case r key pressed: Now drawing red shapes")
    changeColor("red")
    
# Function to switch to drawing yellow shapes
def yKey(event):
    print("Lower case y key pressed: Now drawing yellow shapes")
    changeColor("yellow")


# Function to draw shapes based on current settings
def drawShape(event):
    # Get the x and y coordinates of the mouse click
    x = event.x
    y = event.y
    # Draw the shape based on the current settings
    if shape == "s":
        canvas.create_rectangle(x, y, x+50, y+50, width=5, outline=color, fill=fillColor)
    else:
        canvas.create_oval(x, y, x+50, y+50, width=5, outline=color, fill=fillColor)

    # Print the mouse click or key press event details
    if event.type == '4': 
        print(f"Mouse click at x = {x}, y = {y}")
    elif event.type == '2':
        print(f"Lowercase h press at x = {x}, y = {y}")

# Bind key events to their corresponding functions
root.bind("<KeyPress-s>", sKey)
root.bind("<KeyPress-c>", cKey)
root.bind("<KeyPress-f>", fKey)
root.bind("<KeyPress-F>", FKey)
root.bind("<KeyPress-r>", rKey)
root.bind("<KeyPress-y>", yKey)

# Bind mouse click event and lowercase h key to drawShape function
canvas.bind("<Button-1>", drawShape)
root.bind("<KeyPress-h>", drawShape)

# Start the main event loop
root.mainloop()