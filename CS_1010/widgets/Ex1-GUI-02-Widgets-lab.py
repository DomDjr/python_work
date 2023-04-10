#Dominick Daito Jr
#Ex 1

import tkinter

#creates a a 300 by 300 window
window = tkinter.Tk()
window.geometry("300x300")

#creates a function that stores the string from the entry wigit and changes the window color based on the string
def ButtonResults():
    EntryResult = Entry1.get()
    #if the string reads red then the window background will turn red
    if EntryResult == "red":
        window.configure(bg = "red")
    #if the string reads blue then the window will turn blue
    if EntryResult == "blue":
        window.configure(bg = "blue")
    #if the string doesnt read blue or red,then the background will turn gray
    if EntryResult != "red" or EntryResult != "blue":
        window.configure(bg = "gray")

#creates an entry widget that has a background of white and text of black
Entry1 = tkinter.Entry(window, bg = "white", fg = "black")
#makes a default text on the entry widget
Entry1.insert(-1, "Enter your name here")
Entry1.grid(row = 1, column = 2)
#creates a label for the entry widget to tell the user what to type of Entry it is 
LabelForEntry = tkinter.Label(window, fg = "white", text = "Color Entry?")
LabelForEntry.grid(row = 0, column = 2)
#creates a button for the entry to tell the user what to type in the Entry widget
ButtonForEntry = tkinter.Button(window, text = "Enter [red], [blue], or [  ]", command = ButtonResults)
ButtonForEntry.grid(row = 2, column = 2)
window.mainloop()