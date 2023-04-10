#Dominick Daito Jr
#Ex 2

import tkinter
window = tkinter.Tk()
window.geometry("300x300")

#holds an integer value for the the radiobuttons.
Radioconnect = tkinter.IntVar()

#defines a function that is used to changed the labels text when the checkboxes or radiobuttons are clicked.
def RadioAndCheckFunction():
    #gets the values of the radiobuttons when clicked and stores it into the variable "RadioResult"
    #Converts the value into a string and stores it into "StrRadioResult"
    RadioResult = Radioconnect.get()
    StrRadioResult = str(RadioResult)
    #Configures the label to concatenate a string and the variable "StrRadioResult"
    Label1.configure(text="RadioButton value is " + StrRadioResult)

    #Uses condition statements to specify when to change the text of the label to True or False
    #if the value of Checkconnect1, Checkconnect2, and Checkconnect3 is zero, then the texts label will be False
    if Checkconnect1.get() == 0 and Checkconnect2.get() == 0 and Checkconnect3.get() == 0:
        label2.configure(text = "False")
        label3.configure(text = "False")
        label4.configure(text = "False")
    #if the value Checkconnect1 is 1 and the value of Checkconnect2 and Checkconnect3 is 0, then label2 text will change
    #to True, while the other two will change to False.
    if Checkconnect1.get() == 1 and Checkconnect2.get() == 0 and Checkconnect3.get() == 0:
        label2.configure(text = "True")
        label3.configure(text = "False")
        label4.configure(text = "False")
    #if the value of Checkconnect2 is one while the others are zero, then the text on label 3 will be True while the
    #others are false.
    if Checkconnect1.get() == 0 and Checkconnect2.get() == 1 and Checkconnect3.get() == 0:
        label2.configure(text = "False")
        label3.configure(text = "True")
        label4.configure(text = "False")
    #if the value of Checkconnect3 is one and the others are zero, the text on label4 will output True while the others
    #will be False.
    if Checkconnect1.get() == 0 and Checkconnect2.get() == 0 and Checkconnect3.get() == 1:
        label2.configure(text = "False")
        label3.configure(text = "False")
        label4.configure(text = "True")
    #if the value of Checkconnect1 and Checkconnect2 is 1 and the value of checkconnect3 is 0 then label2 and label3
    #will be True. label4 will output False.
    if Checkconnect1.get() == 1 and Checkconnect2.get() == 1 and Checkconnect3.get() == 0:
        label2.configure(text = "True")
        label3.configure(text = "True")
        label4.configure(text = "False")
    #if the value of Checkconnect2 and Checkconnect3 is one and the value of Checkconnect1 is zero, then label2 will be
    #False while label3 and label4 will be True
    if Checkconnect1.get() == 0 and Checkconnect2.get() == 1 and Checkconnect3.get() == 1:
        label2.configure(text = "False")
        label3.configure(text = "True")
        label4.configure(text = "True")
    #if the value of Checkconnect1 and Checkconnect4 are 1 and the value of Checkconnect2 is 0, then the text of label1 
    #and lanel4 will output True. label3 will output false
    if Checkconnect1.get() == 1 and Checkconnect2.get() == 0 and Checkconnect3.get() == 1:
        label2.configure(text = "True")
        label3.configure(text = "False")
        label4.configure(text = "True")
    #if the value of Checkconnect1 and Checkconnect2 and Checkconnect3 are one, then the texts on label2, label3, and label4
    #will all output True.
    if Checkconnect1.get() == 1 and Checkconnect2.get() == 1 and Checkconnect3.get() == 1:
        label2.configure(text = "True")
        label3.configure(text = "True")
        label4.configure(text = "True")

#creates three radiobuttons with different values and texts
RadioButton1 = tkinter.Radiobutton(window, text = "RadioButton1", variable = Radioconnect, value = 1)

RadioButton2 = tkinter.Radiobutton(window, text = "RadioButton2", variable = Radioconnect, value = 2)

RadioButton3 = tkinter.Radiobutton(window, text = "RadioButton3", variable = Radioconnect, value = 3)

#packs the buttons onto the window
RadioButton1.pack()
RadioButton2.pack()
RadioButton3.pack()

#creates a label for the radio buttons and packs it onto the window
Label1 = tkinter.Label(window, text = "---", font=("Times New Roman", 20))
Label1.pack()

#creates a connection with the checkboxes with output values that are booleans (0 and 1)
Checkconnect1 = tkinter.BooleanVar()
Checkconnect2 = tkinter.BooleanVar()
Checkconnect3 = tkinter.BooleanVar()

#creates three checkboxes with different texts and is assigned different variables with the same value.
CheckButton1 = tkinter.Checkbutton(window, text = "Checkbutton 1", variable = Checkconnect1)
CheckButton2 = tkinter.Checkbutton(window, text = "Checkbutton 2", variable = Checkconnect2)
CheckButton3 = tkinter.Checkbutton(window, text = "Checkbutton 3", variable = Checkconnect3)

#packs the checkboxes onto the window
CheckButton1.pack()
CheckButton2.pack()
CheckButton3.pack()

#creates three labels for the checkboxes to display the values when checked or not.
label2 = tkinter.Label(window, text = "---", font=("Times New Roman", 20))
label3 = tkinter.Label(window, text = "---", font=("Times New Roman", 20))
label4 = tkinter.Label(window, text = "---", font=("Times New Roman", 20))

#packs the labels onto the window
label2.pack()
label3.pack()
label4.pack()

#creates a button for the radiobuttons and checkboxes. When clicked will display the values onto the labels.
ButtonResult = tkinter.Button(window, text = "push for results", command = RadioAndCheckFunction)

#packs the button onto the window
ButtonResult.pack()

#Runs the gui
window.mainloop()