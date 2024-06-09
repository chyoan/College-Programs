# Import all from tkinter
from tkinter import *

# Function to handle radio button selection
def select():
    # Check which radio button is selected
    if radioVar.get() == 1:
        # Change label background to red
        label['bg'] = 'red'
        # Change label text
        label['text'] = 'You selected option 1'
    # Check which radio button is selected
    elif radioVar.get() == 2:
        # Change label background to green
        label['bg'] = 'green'
        # Change label text
        label['text'] = 'You selected option 2'
    elif radioVar.get() == 3:
        # Change label background to blue
        label['bg'] = 'blue'
        # Change label text
        label['text'] = 'You selected option 3'
        
# Create main window
root = Tk()
# Set window title
root.title("Radio Button")

# Create a StringVar to manage radio button selection
radioVar = IntVar()
# Set default radio button selection
radioVar.set("None")

# Create red radio button
radio1 = Radiobutton(root, text="Red", value=1, variable=radioVar, command=select)
# Pack red radio button
radio1.pack(anchor=W)
# Create green radio button
radio2 = Radiobutton(root, text="Green", value=2, variable=radioVar, command=select)
# Pack green radio button
radio2.pack(anchor=W)
# Create blue radio button
radio3 = Radiobutton(root, text="Blue", value=3, variable=radioVar, command=select)
# Pack blue radio button
radio3.pack(anchor=W)

# Create a label
label = Label(root, text="No selection", bg='brown')
# Pack label
label.pack()

# Start main event loop
root.mainloop()