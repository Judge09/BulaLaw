# Imports module from Tcl for GUI
from tkinter import *
from tkinter import ttk

# Basics
# Initialization of Tkinter
# root ung pinaka window
root = Tk()

# Basic buttons
button = ttk.Button(root, text = 'click me')
button.pack()  # Type of Lay out for Gui. (pack as in, just packs them in the window)

### CheckButton
# Declaration
checkbutton = ttk.Checkbutton (root, text = "Valorantz")
checkbutton.pack() # Lay out
# Declaration of String variable
string = StringVar()
# String output
string.set('Egoist')
#Config of CheckButton w/ onvalue & offvalue
checkbutton.config(variable = string, onvalue = 'Duelist', offvalue = 'Sentinel')

### RadioButton
# Declaration of String
Val = StringVar()

# Buttons and Values
ttk.Radiobutton (root, text = 'Duelist', variable = Val, value = 'Egoist').pack()
ttk.Radiobutton (root, text = 'Initiator', variable = Val, value = 'Concuss').pack()
ttk.Radiobutton (root, text = 'Sentinel', variable = Val, value = 'Healer').pack()

### type '{VariableName}.get()' to get the output of the button variables