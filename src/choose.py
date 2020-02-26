from tkinter import *
import random

def choose():
    global temp, students

    if(len(temp) == 0):
        temp = students.copy()

    student = random.choice(temp)
    chosen.config(text = "" + student, font = "calibri 20 bold")
    temp.remove(student)
    left.config(text = "Left : " + str(len(temp)), font = "calibri 16")

students = []
temp = []

try:
    file = open("list.txt")
    students = [line[:-1] for line in file]
    file.close()

except:
    exit(1)

window = Tk()
window.tk_setPalette("#1abc9c")
window.title("Choose!")
window.geometry("500x275+250+250")

opening = Label(window, pady = 10)
opening.config(text = "Next student:", font = "calibri 16")
opening.pack()

chosen = Label(window, pady = 20)
chosen.config(text = "Did not chosen!", font = "calibri 20 bold")
chosen.pack()

left = Label(window, pady = 10)
left.config(text = "Left : " + str(len(students)), font = "calibri 16")
left.pack()

blank = Label(window)
blank.pack()

button = Button(window)
button.config(text = "Choose!", font = "calibri 16", command = choose)
button.pack()

window.mainloop()
