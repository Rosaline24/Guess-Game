#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import random

top = Tkinter.Tk()
top.title('Guess Game')

def goBtn():
    L2v.set("")
    real=makeAns()
    a=0
    global go
    go=1
    global inner
    def inner():
        if(L2v.get()!='You win!'):
            if(isDigit()!=True):
                L2v.set("It's not number, please enter 4 numbers.")
                #ansStr=map(int,str(input.get()))
            elif(len(input.get())!=4):
                L2v.set("Please enter 4 numbers.")
            else:
                ansStr=map(int,str(input.get()))
                if( ansStr[0]!=ansStr[1] and ansStr[0]!=ansStr[2] and ansStr[0]!=ansStr[3] and
                    ansStr[1]!=ansStr[2] and ansStr[1]!=ansStr[3] and ansStr[2]!=ansStr[3]):
                    print(ansStr)
                    L2v.set("") #clear the label
                    check(real,ansStr)
                else:
                    L2v.set("Please enter 4 different numbers.")
    inner()

def next():
    global go
    go=2
    inner()

def isDigit():
    try:
        int(input.get())
    except ValueError:
        return False
    else:
        return True

def makeAns():
    rightAns=list(random.sample(range(0,9),4))
    print(rightAns)
    return rightAns

def check(A,B):
    a=0
    b=0
    #find A
    if(A[0]==B[0]):
        global a
        a+=1
    if(A[1]==B[1]):
        a+=1
    if(A[2]==B[2]):
        a+=1
    if(A[3]==B[3]):
        a+=1
        print(a)
    #find B
    if(A[0]==B[1] or A[0]==B[2] or A[0]==B[3]):
        global b
        b+=1
    if(A[1]==B[0] or A[1]==B[2] or A[1]==B[3]):
        b+=1
    if(A[2]==B[0] or A[2]==B[1] or A[2]==B[3]):
        b+=1
    if(A[3]==B[0] or A[3]==B[1] or A[3]==B[2]):
        b+=1
        print(b)
    aaa=str(a)+'A'+str(b)+'B'
    bbb=input.get()+aaa
    if(a==4 and b==0):
        L2v.set('You win!')
    else:
        # def showText(string,append):
        #     if(append==False):
                L4v.set(input.get()+" "+aaa+"\n")#str(a)+'A'+str(b)+'B'
            # else:
            #     print()
        # if(go==1):
        #     showText(aaa,False)
        #     print('f')
        # else:
        #     showText(bbb,True)
        #     print('t')


size=Tkinter.Frame(master=top,width=500,height=50) #width=500,height=500
size.pack()

L1=Tkinter.Label(top,textvariable='請輸入4個數字：')#padx pady
L1.pack()

inputVar=Tkinter.StringVar()
input=Tkinter.Entry(top,textvariable=inputVar)
input.pack()

result=Tkinter.Button(top, text='Go',command=goBtn)
resultStr=Tkinter.StringVar()
result.pack()

next=Tkinter.Button(top, text='Next',command=next)#command=nextBtn
next.pack()

ansVar=Tkinter.IntVar()
aaa=Tkinter.StringVar()

L2v=Tkinter.StringVar()
L2=Tkinter.Label(top,textvariable=L2v)
L2.pack()

L3v=Tkinter.StringVar()
L3=Tkinter.Label(top,textvariable=L3v)
L3.pack()

L4v=Tkinter.StringVar()
L4=Tkinter.Label(top,textvariable=L4v)
L4.pack()

top.mainloop()
