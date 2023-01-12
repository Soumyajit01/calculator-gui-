from tkinter import *
root = Tk()
# root.geometry("500x500")
root.title("CALCULATOR")
root.resizable(False, False)
l = Label(text="CALCULATOR", font="Monetizer 30")
l.pack()
frame1 = Frame(root, relief=SUNKEN)
num1 = Label(frame1,text="Number 1: ",font=("Courier 15 bold"))
num1.pack(side=LEFT, anchor='nw')
inp1= Entry(frame1, width= 30, font=("Courier 15 bold"))
inp1.pack()
frame1.pack()

frame2 = Frame(root, relief=SUNKEN)
num2 = Label(frame2,text="Number 2: ",font=("Courier 15 bold"))
num2.pack(side=LEFT)
inp2= Entry(frame2, width= 30, font=("Courier 15 bold"))
inp2.pack()
frame2.pack(pady=15)

def getNum():
    global inp1
    inputNum1= int(inp1.get())
    global inp2
    inputNum2= int(inp2.get())

def add():
    getNum()
    global inp1
    inputNum1= int(inp1.get())
    global inp2
    inputNum2= int(inp2.get())
    answer.config(text=inputNum1+inputNum2)
def subtract():
    global inp1
    inputNum1= int(inp1.get())
    global inp2
    inputNum2= int(inp2.get())
    answer.config(text=inputNum1-inputNum2)
def divide():
    global inp1
    inputNum1= int(inp1.get())
    global inp2
    inputNum2= int(inp2.get())
    try:
        answer.config(text=round(inputNum1/inputNum2, 2))
    except ZeroDivisionError as e:
        answer.config(text="(undefined)")
def multiply():
    global inp1
    inputNum1= int(inp1.get())
    global inp2
    inputNum2= int(inp2.get())
    answer.config(text=inputNum1*inputNum2)
    

frame3 = Frame(root, borderwidth=4, relief=SUNKEN)
add = Button(frame3, fg = "blue", text="+", font="Monetizer 20", command=add)
subtract = Button(frame3, fg = "blue", text="-", font="Monetizer 20", command=subtract)
divide = Button(frame3, fg = "blue", text="/", font="Monetizer 20", command=divide)
multiply = Button(frame3, fg = "blue", text="x", font="Monetizer 20", command=multiply)
add.pack(side=LEFT)
subtract.pack(side=LEFT)
divide.pack(side=LEFT)
multiply.pack(side=LEFT)
close = Button(root, fg = "blue", text="CLOSE CALCULATOR", font="Monetizer 20", command = quit)
answer = Label(root, width= 30, font=15, text="")
answer.pack()
close.pack(side=BOTTOM)
frame3.pack(side=LEFT, anchor='nw', padx=200)
