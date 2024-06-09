# Import all from tkinter
from tkinter import *

# Function to handle button click for copying text
def copyTextToLabel():
    # Check if entry is empty
    if len(variable.get()) == 0:
        # Change button color to red
        button['bg'] = 'red'
    else:
        # Update label text with entry text
        label['text'] = variable.get()
        # Print entry text
        print(entry.get())
        # Reset button color
        button['bg'] = buttonBgColor
        # Change button text to "Clear Text"
        button['text'] = "Clear Text"
        # Change button command to clear entry text
        button['command'] = clearEntryText
        

# Function to handle clearing text
def clearEntryText():
    # Clear entry text
    variable.set('')
    # Change button text to "Copy Text"
    button['text'] = "Copy Text"
    # Change button command to copy text to label
    button['command'] = copyTextToLabel

# Create main window
root = Tk()
# Create window title
root.title("Adding a Label and Entry Widget")
# Create window dimensions
root.geometry('200x100')

# Create label
label = Label(root, text="Text is displayed here")
# Pack label at bottom
label.pack(side=BOTTOM)

# Create button
button = Button(root, text="Copy Text", command=copyTextToLabel)
# Set original bg color of button
buttonBgColor = button['bg']
# Pack button at bottom
button.pack(side=BOTTOM)

# Create a StringVar to manage entry text
variable = StringVar()
# Create entry with variable text
entry = Entry(root, textvariable=variable)
# Pack entry at bottom
entry.pack(side=BOTTOM)

# Start main event loop
root.mainloop()