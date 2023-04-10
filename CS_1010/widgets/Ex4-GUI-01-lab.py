#Dominick Daito Jr
#Ex-4

import tkinter
groot = tkinter.Tk()

import random
random_number = random.randint(1,100)

#creates a window that is 300 by 300 pixels.
groot.geometry("300x300")

#changes the background color to blue
groot.configure(bg = "blue")

#Makes a title for the created window
groot.title("My Favorite Color")

#creates a function for the first button that will change the first label when pushed.
def doButton():
    groot_label.configure(text = "first button has been pushed")

#creates a blue background label that outputs a text and packs it onto the window
groot_label = tkinter.Label(groot, text = "Here is the first button", bg = "blue")
groot_label.pack()
#creates another blue background label that outputs a text and packs it onto the window
groot_label2 = tkinter.Label(groot, text= "Click the button", bg = "blue")
groot_label2.pack()

#creates a green background color that outputs a text and calls the "doButton" function when clicked on
groot_button1 = tkinter.Button(groot, text = "Button ONE", highlightbackground = "green", command=doButton)
#packs the button on the window
groot_button1.pack()

#creates a function for the second button that will change the first and second label
def doButton2():
    groot_label.configure(text = "here is a random number")
    groot_label2.configure(text = random_number )

#creates a second button that is has a background of red, prints out a text, and calls the "doButton2" function when clicked on
groot_button2 = tkinter.Button(groot, text = "Button TWO", highlightbackground = "red", command=doButton2)
#customizes the buttons height and width
groot_button2.configure(height = 2, width = 10)
#packs the button onto the window
groot_button2.pack()

#runs the GUI with the two labels and background.
groot.mainloop()