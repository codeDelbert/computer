from tkinter import *
from tkinter import messagebox
import math

W1 = Tk()
W1.title('簡單的計算機')
W2 = Tk()
Ans1 = messagebox.askquestion('在開計算機前請先回答','陳晉帥嗎?')

if Ans1 == 'yes':
    Ans2 = messagebox.askquestion('竟然!!','你竟然覺得帥!')
else:
    Ans3 = messagebox.showinfo('恭喜!','我也是這麼覺得')

if Ans2 =='yes':
    messagebox.showerror('你還繼續選yes!','你腦子壞了')
else:
    messagebox.showerror('知錯能改善莫大焉','看你腦袋還算正常')

def btnclick(numbers):
    inputBox.insert(END,numbers)

def btnClear():
    inputBox.delete(0,END)

def btnEqual():
    result = eval(inputBox.get())
    inputBox.delete(0,END)
    inputBox.insert(0,result)

def btnBack():
    lastletter = len(inputBox.get())-1
    inputBox.delete(lastletter,END)

def btnPower():
    result = eval(inputBox.get())
    result = pow(result,2)
    inputBox.delete(0,END)
    inputBox.insert(0,result)

def btnRoot():
    result = eval(inputBox.get())
    result = math.sqrt(result)
    inputBox.delete(0,END)
    inputBox.insert(0,result)

inputBox = Entry(W1,bd = 20,font = 30)
inputBox.grid(row = 0,columnspan = 3)

bX = Button(W1,padx = 10,pady = 16,bd = 8,text = '作者',command = lambda : btnclick("哈囉 我是作者陳子航:D"))

b1 = Button(W1,padx = 16,pady = 16,bd = 8,text = '1',command = lambda : btnclick(1))
b2 = Button(W1,padx = 16,pady = 16,bd = 8,text = '2',command = lambda : btnclick(2))
b3 = Button(W1,padx = 16,pady = 16,bd = 8,text = '3',command = lambda : btnclick(3))
bADD = Button(W1,padx = 16,pady = 16,bd = 8,text = '+',command = lambda : btnclick('+'))

b4 = Button(W1,padx = 16,pady = 16,bd = 8,text = '4',command = lambda : btnclick(4))
b5 = Button(W1,padx = 16,pady = 16,bd = 8,text = '5',command = lambda : btnclick(5))
b6 = Button(W1,padx = 16,pady = 16,bd = 8,text = '6',command = lambda : btnclick(6))
bSUB = Button(W1,padx = 16,pady = 16,bd = 8,text = '-',command = lambda : btnclick('-'))

b7 = Button(W1,padx = 16,pady = 16,bd = 8,text = '7',command = lambda : btnclick(7))
b8 = Button(W1,padx = 16,pady = 16,bd = 8,text = '8',command = lambda : btnclick(8))
b9 = Button(W1,padx = 16,pady = 16,bd = 8,text = '9',command = lambda : btnclick(9))
bMUL = Button(W1,padx = 16,pady = 16,bd = 8,text = '*',command = lambda : btnclick('*'))

bDIV = Button(W1,padx = 16,pady = 16,bd = 8,text = '/',command = lambda : btnclick('/'))
bDot = Button(W1,padx = 16,pady = 16,bd = 8,text = '.',command = lambda : btnclick('.'))
bClear = Button(W1,padx = 16,pady = 16,bd = 8,text = 'C',command = lambda : btnClear())
b0 = Button(W1,padx = 16,pady = 16,bd = 8,text = '0',command = lambda : btnclick(0))

bRoot = Button(W1,padx = 16,pady = 16,bd = 8,text = '√',command = lambda : btnRoot())
bPow = Button(W1,padx = 16,pady = 16,bd = 8,text = 'P',command = lambda : btnPower())
bBS = Button(W1,padx = 16,pady = 16,bd = 8,text = '←',command = lambda : btnBack())
bEQ = Button(W1,padx = 16,pady = 16,bd = 8,text = '↵',command = lambda : btnEqual())

b1.grid(row = 1,column = 0)
b2.grid(row = 1,column = 1)
b3.grid(row = 1,column = 2)
bADD.grid(row = 1,column = 4)

b4.grid(row = 2,column = 0)
b5.grid(row = 2,column = 1)
b6.grid(row = 2,column = 2)
bSUB.grid(row = 2,column = 4)

b7.grid(row = 3,column = 0)
b8.grid(row = 3,column = 1)
b9.grid(row = 3,column = 2)
bMUL.grid(row = 3,column = 4)

bDot.grid(row = 4,column = 0)
b0.grid(row = 4,column = 1)
bClear.grid(row = 4,column = 2)
bDIV.grid(row = 4,column = 4)

bRoot.grid(row = 5,column = 0)
bPow.grid(row = 5,column = 1)
bBS.grid(row = 5,column = 2)
bEQ.grid(row = 5,column = 4)

bX.grid(row = 0,column = 4)
            
W1.mainloop()