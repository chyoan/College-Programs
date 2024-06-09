# Import all from tkinter
from tkinter import *

# Create main window
root = Tk()
# Set window title
root.title("Managing Layout")

# Create left frame with groove border and border width of 5
leftFrame = Frame(root, bd=5, relief=GROOVE)
# Create right frame with groove border and border width of 5
rightFrame = Frame(root, bd=5, relief=GROOVE)
# Pack left frame to the left side, fill both directions, and allow expansion
leftFrame.pack(side=LEFT, fill=BOTH, expand=1)
# Pack right frame to the right side, fill both directions, and allow expansion
rightFrame.pack(side=RIGHT, fill=BOTH, expand=1)

# Create label b1 in left frame with blue background and width of 12
b1 = Label(leftFrame, text="A", bg='blue', width=12)
# Create label b2 in left frame with white background and width of 12
b2 = Label(leftFrame, text="B", bg='white', width=12)
# Create label b3 in right frame with white background and width of 12
b3 = Label(rightFrame, text="C", bg='white', width=12)
# Create label b4 in right frame with blue background and width of 12
b4 = Label(rightFrame, text="D", bg='blue', width=12)

# Pack label b1 at the top of left frame, fill both directions, and allow expansion
b1.pack(side=TOP, fill=BOTH, expand=1)
# Pack label b2 at the bottom of left frame, fill both directions, and allow expansion
b2.pack(side=BOTTOM, fill=BOTH, expand=1)
# Pack label b3 at the top of right frame, fill both directions, and allow expansion
b3.pack(side=TOP, fill=BOTH, expand=1)
# Pack label b4 at the bottom of right frame, fill both directions, and allow expansion
b4.pack(side=BOTTOM, fill=BOTH, expand=1)

# Start the main loop
root.mainloop()