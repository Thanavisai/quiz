from tkinter import *

Questions = ["Who developed Python Programming Language?",
             "Is Python case sensitive when dealing with identifiers?",
             "Which of the following is the correct extension of the Python file?",
             "Which of the following is used to define a block of code in Python language?",
             " Which of the following character is used to give single-line comments in Python?",
             "Which keyword is used for function in Python language?",
             "Python supports the creation of anonymous functions at runtime, using a construct called __________",
             "Which of the following is the truncation division operator in Python?",
              "Which of the following is the use of id() function in python?",
             "Which of the following is not a core data type in Python programming?"]
Options = [["Wick van Rossum","Rasmus Lerdorf","Guido van Rossum"],[" no","yes","machine dependent"],
           [".py",".python",".pyt"],[" Indentation","Key","Brackets"],["//","#","\*"],
           ["Function","fun","def"],["pi","anonymous","lambda"],["|","//","\\"],
           [" Every object doesn’t have a unique id","Id returns the identity of the object","All of the mentioned"],
           ["Tuples","Lists","Class"]]

Answers = [3,2,1,1,2,3,3,2,2,3]

Score = 0
Total_No_Questions = 10
Question_no = 1


def next():
    global Score, Question_no
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers[Question_no-1] == selected_option :
        Score += 1

    Question_no += 1

    if Question_no > Total_No_Questions:
        root.pack_forget()
        score.place(relx=.40, rely=.40)
        score.config(text="Your Score:"+str(Score)+"/10", font=("Arial", 20))

    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=Questions[Question_no-1])
        option1.config(text=Options[Question_no-1][0])
        option2.config(text=Options[Question_no-1][1])
        option3.config(text=Options[Question_no-1][2])


def check(option):
    if option == 1:
        val2.set(0)
        val3.set(0)
    elif option == 2:
        val1.set(0)
        val3.set(0)
    else:
        val2.set(0)
        val1.set(0)


Win = Tk()
Win.title("Quiz Application")


root = Frame()
root.pack()

name=Label(root, width=60,height=1, font=("Arial",24), bg="Orange", text="GET STARTED WITH YOUR ONLINE QUIZ ON PYTHON PROGRAMMING")
name.pack()


question = Label(root, width=60, bg="#fff", font=("Arial", 20), text=Questions[0])
question.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root, font=("Arial",15), variable=val1, text=Options[0][0], command=lambda: check(1))
option1.pack()

option2 = Checkbutton(root, font=("Arial",15), variable=val2, text=Options[0][1], command=lambda: check(2))
option2.pack()

option3 = Checkbutton(root, font=("Arial",15), variable=val3, text=Options[0][2], command=lambda: check(3))
option3.pack()

next_b = Button(root,font=("Arial",20), text="next", command=next)
next_b.pack()

score = Label(Win)
score.place_forget()

mainloop()