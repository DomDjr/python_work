from tkinter import *
#Creates a mainwindow for frames to stack on
MainWindow = Tk()
MainWindow.geometry("400x400")
MainWindow.title("Simple Quiz")
MainWindow.configure(bg = "Red")

RadioConnect = StringVar()
CheckButtonConnect1 = IntVar()
CheckButtonConnect2 = IntVar()
CheckButtonConnect3 = IntVar()
LifeCounter3 = str(3)
LifeCounter2 = str(3)
LifeCounter1 = str(3)

#Creates a function for the question three answers once the enter button is clicked
def QuestionThreeRadioConnect():
    if RadioConnect.get() == "B":
        QuestionThreeAnswerLabel.configure(text = "Correct")
        WinningFrame.tkraise()
    if RadioConnect.get() != "B":
        QuestionThreeAnswerLabel.configure(text = "Wrong")
        global LifeCounter3
        LifeCounter3 = int(LifeCounter3)
        LifeCounter3 -= 1
        LifeCounter3 = str(LifeCounter3)
        QuestionThreeLifeCounter.configure(text = LifeCounter3 + " Lives")
    if LifeCounter3 == "0":
        MainWindow.destroy()

def QuestionTwoEntryButton():
    if QuestionTwoEntry.get() == "7":
        QuestionTwoLabelAnswer.configure(text = "Correct", font = ("Times New Roman", 10), width = 10, height = 5)
        QuestionThreeFrame.tkraise()
    if QuestionTwoEntry.get() != "7":
        QuestionTwoLabelAnswer.configure(text = "Try Again", font = ("Times New Roman", 10), width = 10, height = 3)
        global LifeCounter2
        LifeCounter2 = int(LifeCounter2)
        LifeCounter2 -= 1
        LifeCounter2 = str(LifeCounter2)
        QuestionTwoLifeCounter.configure(text = LifeCounter2 + " Lives")
    if LifeCounter2 == "0":
        MainWindow.destroy()

def QuestionOneCheckButton():
    if CheckButtonConnect1.get() == 1 and CheckButtonConnect2.get() == 0 and CheckButtonConnect3.get() == 0:
        QuestionOneLabel.configure(text = "Correct", fg = "white")
        QuestionTwoFrame.tkraise()
    if CheckButtonConnect1.get() == 0 and CheckButtonConnect2.get() == 1 and CheckButtonConnect3.get() == 0:
        QuestionOneLabel.configure(text = "wrong", fg = "white")
        global LifeCounter1
        LifeCounter1 = int(LifeCounter1)
        LifeCounter1 -= 1
        LifeCounter1 = str(LifeCounter1)
        QuestionOneLifeCounter.configure(text = LifeCounter1 + " Livess")
    if CheckButtonConnect1.get() == 0 and CheckButtonConnect2.get() == 0 and CheckButtonConnect3.get() == 1:
        QuestionOneLabel.configure(text = "wrong", fg = "white")
        LifeCounter1 = int(LifeCounter1)
        LifeCounter1 -= 1
        LifeCounter1 = str(LifeCounter1)
        QuestionOneLifeCounter.configure(text = LifeCounter1 + " Livess")
    if CheckButtonConnect1.get() == 1 and CheckButtonConnect2.get() == 1 and CheckButtonConnect3.get() == 0:
        QuestionOneLabel.configure(text = "wrong", fg = "white")
        LifeCounter1 = int(LifeCounter1)
        LifeCounter1 -= 1
        LifeCounter1 = str(LifeCounter1)
        QuestionOneLifeCounter.configure(text = LifeCounter1 + " Livess")
    if CheckButtonConnect1.get() == 1 and CheckButtonConnect2.get() == 0 and CheckButtonConnect3.get() == 1:
        QuestionOneLabel.configure(text = "wrong", fg = "white")
        LifeCounter1 = int(LifeCounter1)
        LifeCounter1 -= 1
        LifeCounter1 = str(LifeCounter1)
        QuestionOneLifeCounter.configure(text = LifeCounter1 + " Livess")
    if CheckButtonConnect1.get() == 0 and CheckButtonConnect2.get() == 1 and CheckButtonConnect3.get() == 1:
        QuestionOneLabel.configure(text = "wrong", fg = "white")
        LifeCounter1 = int(LifeCounter1)
        LifeCounter1 -= 1
        LifeCounter1 = str(LifeCounter1)
        QuestionOneLifeCounter.configure(text = LifeCounter1 + " Lives")
    if LifeCounter1 == "0":
        MainWindow.destroy()

def TitleScreenButton():
    if QuizTitleEntryBox.get() != "Enter Your Name":
        QuestionOneFrame.tkraise()

#Creates a winning frame once the user correctly answers question three
WinningFrame = Frame(MainWindow, bg = "Blue")
WinningFrame.place(x = 25, y = 25, relheight = 0.87, relwidth = 0.87)
WinningFrameLabel = Label(WinningFrame, text = "You won", font = ("Times New Roman", 40, "italic"), fg = "white", bg = "blue")
WinningFrameLabel.place(x = 110, y = 130, relheight = 0.30, relwidth = 0.40)

#Creates a frame for question three
QuestionThreeFrame = Frame(MainWindow, bg = "blue")
QuestionThreeFrame.place(x = 25, y = 25, relheight = 0.87, relwidth = 0.87)

#Creates a question for question three
QuestionThreeLabel = Label(QuestionThreeFrame, text = "What month is Christmas?", fg = "white", bg = "blue", font = ("Times New Roman", 20))
QuestionThreeLabel.place(x = 45, y = 10, relheight = 0.30, relwidth = 0.70)

#Creates an answer list out of radiobuttons
QuestionThreeRadioButton1 = Radiobutton(QuestionThreeFrame, text = "November", variable = RadioConnect, value = "A", fg = "white", bg = "blue")
QuestionThreeRadioButton2 = Radiobutton(QuestionThreeFrame, text = "December", variable = RadioConnect, value = "B", fg = "white", bg = 'blue')
QuestionThreeRadioButton3 = Radiobutton(QuestionThreeFrame, text = "January", variable = RadioConnect, value = "C", fg = "white", bg = "blue")

QuestionThreeRadioButton1.place(x = 50, y = 140, relheight = 0.05, relwidth = 0.70)
QuestionThreeRadioButton2.place(x = 50, y = 160, relheight = 0.05, relwidth = 0.70)
QuestionThreeRadioButton3.place(x = 50, y = 180, relheight = 0.05, relwidth = 0.70)

#Creates a label for the life counter in question three
QuestionThreeLifeCounter = Label(QuestionThreeFrame, text = LifeCounter3 + " Lives", bg = "blue", fg = "white", font = ("Times New Roman", 15))
QuestionThreeLifeCounter.place(x = 280, y = 300, relheight = 0.10, relwidth = 0.15)

#Creates a label for a filler in question three to let the user know if they got it wrong
QuestionThreeAnswerLabel = Label(QuestionThreeFrame, text = "---", fg = "white", bg = "blue", font = ("Times New Roman", 10))
QuestionThreeAnswerLabel.place(x = 160, y = 100, relheight = 0.10, relwidth = 0.10)

#Creates a button for question three
QuestionThreeEnterButton = Button(QuestionThreeFrame, text = "Enter", fg = "white", bg = "blue", font = (10), command = QuestionThreeRadioConnect)
QuestionThreeEnterButton.place(x = 145, y = 250, relheight = 0.10, relwidth = 0.20)

#Creates a frame for question two
QuestionTwoFrame = Frame(MainWindow, bg = "blue")
QuestionTwoFrame.place(x = 25, y = 25, relheight = 0.87, relwidth = 0.87)

#Creates a question for question two
QuestionTwoLabel = Label(QuestionTwoFrame, text = "How many days are in a week?", fg = "white", bg = "blue", font = ("Times New Roman", 20))
QuestionTwoLabel.place(x = 45, y = 10, relheight = 0.30, relwidth = 0.75)

#Creates an answer box for the user to fill in
QuestionTwoEntry = Entry(QuestionTwoFrame, text = "Enter Your Answer", fg = "white", bg = "blue")
QuestionTwoEntry.insert(END, "Enter Your Answer")
QuestionTwoEntry.place(x = 115, y = 250, relheight = 0.10, relwidth = 0.37)

#Creates a label to let the user know if they got it wrong or right
QuestionTwoLabelAnswer = Label(QuestionTwoFrame, text = "---", fg = "white", bg = "blue", font = ("Times New Roman", 5))
QuestionTwoLabelAnswer.place(x = 140, y = 200, relwidth = 0.20)

#Creates a button for Question two
QuestionTwoButton = Button(QuestionTwoFrame, text = "Enter", fg = "white", bg = "blue", command = QuestionTwoEntryButton)
QuestionTwoButton.place(x = 150, y = 300)

#Creates a life counter for question two
QuestionTwoLifeCounter = Label(QuestionTwoFrame, text = LifeCounter2 + " Lives", bg = "blue", fg = "white", font = ("Times New Roman", 15))
QuestionTwoLifeCounter.place(x = 280, y = 300, relheight = 0.10, relwidth = 0.15)

#Creates a frame for question three
QuestionOneFrame = Frame(MainWindow, bg = "blue")
QuestionOneFrame.place(x = 25, y = 25, relheight = 0.87, relwidth = 0.87)

#Creates a question for question for question one
QuestionOneLabel = Label(QuestionOneFrame, text = "How many states are in the US?", fg = "white", bg = "blue", font = ("Times New Roman", 20))
QuestionOneLabel.place(x = 25, y = 10, relheight = 0.30, relwidth = 0.87)

#Creates checkbutton so the user can select answers
Q1CheckButton1 = Checkbutton(QuestionOneFrame, text = "50", variable = CheckButtonConnect1, onvalue = 1, offvalue = 0, bg = "blue")
Q1CheckButton1.place(x = 150, y = 100, relwidth = 0.30)
Q1CheckButton2 = Checkbutton(QuestionOneFrame, text = "51", variable = CheckButtonConnect2, onvalue = 1, offvalue = 0, bg = "blue")
Q1CheckButton2.place(x = 150, y = 120, relwidth = 0.30)
Q1CheckButton3 = Checkbutton(QuestionOneFrame, text = "49", variable = CheckButtonConnect3, onvalue = 1, offvalue = 0, bg = "blue")
Q1CheckButton3.place(x = 150, y = 140, relwidth = 0.30)

#Creates a button for the CheckButtons
QuestionOneButton = Button(QuestionOneFrame, text = "Enter", font = ("Times New Roman", 20), command = QuestionOneCheckButton)
QuestionOneButton.place(x = 130, y = 250, relheight = 0.10, relwidth = 0.30)

#Creates a label for question one to tell the user if they got the question right or wrong
QuestionOneLabel = Label(QuestionOneFrame, text = "---", font = ("Times New Roman", 20), fg = "blue", bg = "blue")
QuestionOneLabel.place(x = 170, y = 180)

#Creates a life counter for question one
QuestionOneLifeCounter = Label(QuestionOneFrame, text = LifeCounter1 + " Lives", bg = "blue", fg = "white", font = ("Times New Roman", 15))
QuestionOneLifeCounter.place(x = 280, y = 300, relheight = 0.10, relwidth = 0.15)

#Creates a title screen for the quiz
QuizTitleScreen = Frame(MainWindow, bg = "blue")
QuizTitleScreen.place(x = 25, y = 25, relheight = 0.87, relwidth = 0.87)

#Creates a title for the title screen
QuizTitleScreenTitle = Label(QuizTitleScreen, text = "Simple Quiz", fg = "white", bg = "blue", font =("Times New Roman", 20))
QuizTitleScreenTitle.place(x = 25, y = 10, relheight = 0.30, relwidth = 0.87)

#Creates instructions for the quiz
QuizInstructionsLabel = Label(text = "You have to answer three questions.", bg = "blue", fg = "white")
QuizInstructionsLabel.place(x = 85, y = 130, relheight = 0.10, relwidth = 0.60)

QuizInstructionsLabel = Label(text = "You have three lives to answer each question.", bg = "blue", fg = "white")
QuizInstructionsLabel.place(x = 65, y = 160, relheight = 0.10, relwidth = 0.70)

#Creates an enter button to go to question one
QuizTitleScreenButton = Button(text = "Enter", font = ("Times New Roman", 10), command = TitleScreenButton)
QuizTitleScreenButton.place( x = 150, y = 300, relheight = 0.10, relwidth = 0.30)

#Creates a name Entry for the user
QuizTitleEntryBox = Entry(text = "Enter", font = ("Times New Roman", 20))
QuizTitleEntryBox.place(x = 150, y = 230, relheight = 0.10, relwidth = 0.30)
QuizTitleEntryBox.insert(END, "Enter Your Name")







MainWindow.mainloop()