# Import all from tkinter, messagebox, and filedialog
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Initialze variables to track the current file, its content, and changes
currentFile = None
currentContent = None
fileChanged = False

# Function to open a file
def openFile():
    global currentFile, currentContent, fileChanged

    # Check for unsaved changes before opening a new file
    if currentFile and currentContent != open(currentFile).read():
        choice = messagebox.askquestion("Unsaved Changes", "Save changes before opening a new file?", default=messagebox.NO)
        if choice == "yes":
            saveFile()

    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            # Read the file content and display it
            with open(file_path, 'r') as file:
                currentContent = file.read()
                currentFile = file_path
                print(currentContent)
        except Exception as e:
            print(f"Failed to open file: {e}")

# Function to save the current file
def saveFile():
    global currentFile, currentContent, fileChanged

    # Show an error if no file is open
    if not currentFile:
        messagebox.showerror("No File", "No file is currently open. Open a file before saving.")
        return

    # Show an info message if no changes are made
    if currentContent == open(currentFile).read():
        messagebox.showinfo("No Changes", "No changes to save.")
        return

    # Open a file dialog to save the file
    file_path = filedialog.asksaveasfilename()
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(currentContent)
                fileChanged = False
        except Exception as e:
            print(f"Failed to save file: {e}")

# Function to quit the application
def quitFile():
    global fileChanged

    # Check for unsaved changes before quitting
    if fileChanged:
        choice = messagebox.askquestion("Unsaved Changes", "Save changes before quitting?", default=messagebox.NO)
        if choice == "yes":
            saveFile()
    else:
        root.destroy()

# Function to convert the text to uppercase
def upperEdit():
    global currentFile, currentContent, fileChanged

    # Show an error if no file is open
    if currentFile is None:
        messagebox.showerror("No file", "No file open")
        return
    else:
        # Convert the text to uppercase
        currentContent = currentContent.upper()
        fileChanged = True

# Function to show help
def aboutHelp():
    messagebox.showinfo("Help", "Useful help.")

# Function to show about information
def aboutAbout():
    messagebox.showinfo("About", "Application to change text file to upper case.")

# Create the main window
root = Tk()
# Set the window title
root.title("Dialogs and Menu")
# Set the window size
root.geometry('400x400')

# Create a menu bar
menu = Menu(root)
# Add the menu to the window
root.config(menu=menu)

# Create the File menu
fle = Menu(menu)
# Add commands to the File menu
fle.add_command(label='Open', command=openFile)
# Add save command to the File menu
fle.add_command(label='Save', command=saveFile)
# Add quit command to the File menu
fle.add_command(label='Quit', command=quitFile)
# Add the File menu to the menu bar
menu.add_cascade(label="File", menu=fle)

# Create the Edit menu
edit = Menu(menu)
# Add the Convert to upper command to the Edit menu
edit.add_command(label='Convert to upper', command=upperEdit)
# Add the Edit menu to the menu bar
menu.add_cascade(label="Edit", menu=edit)

# Create the Help menu
hlp = Menu(menu)
# Add commands to the Help menu
hlp.add_command(label='Help', command=aboutHelp)
# Add about command to the Help menu
hlp.add_command(label='About', command=aboutAbout)
# Add the Help menu to the menu bar
menu.add_cascade(label="Help", menu=hlp)

# Start the main event loop
root.mainloop()