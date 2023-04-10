#Dominick Daito Jr
#Ex-3

import tkinter
groot = tkinter.Tk()

#creates a window that is 300 by 300 pixels.
groot.geometry("300x300")

#changes the background color to blue
groot.configure(bg = "blue")

#Makes a title for the created window
groot.title("My Favorite Color")

#creates a label that outputs the text "A label"
groot_label = tkinter.Label(groot, text= "A label")

#packs it onto the window
groot_label.pack()

#creates another label that turns the label's background red and the font color green.
#Changes the font to "Times New Roman", the font size to 30, and the text to italics.
groot_label2 = tkinter.Label(groot, text= "A second label", bg= "red", fg= "green", font = ("Times New Roman", 30, "italic"))

#packs the second label onto the window
groot_label2.pack()

#runs the GUI with the two labels and background.
groot.mainloop()