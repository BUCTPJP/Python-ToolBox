import tkinter as tk
from tkinter import DISABLED, END, INSERT, NORMAL, RAISED, SUNKEN, font

 #主窗体
window = tk.Tk()
window.title('小工具盒')
window.geometry('800x600+400+100')
window.iconbitmap('ico.ico')
window.configure(bg = 'lemonchiffon')

 #定义函数
def show1():
    height = eval(e1.get())
    weight = eval(e2.get())
    BMI = weight / pow(height,2)
    a = 'BMI的数值位:{:.2f}'.format(BMI)
    if BMI < 18.5:
        INT,DOM = '偏瘦','偏瘦'
    elif 18.5 <= BMI <24:
        INT,DOM = '正常','正常'
    elif 24 <= BMI < 25:
        INT,DOM = '正常','偏胖'
    elif 25 <= BMI < 28:
        INT,DOM = '偏胖','偏胖'
    elif 28 <= BMI < 30:
        INT,DOM = '偏胖','肥胖'
    else:
        INT,DOM = '肥胖','肥胖'
    b = "BMI的指标为:国际'{0}'，国内'{1}'".format(INT,DOM)
    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,a)
    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,'\n')
    showarea.insert(END,b)

def show2():
    TempStr = e3.get()
    if TempStr[-1] in ['F','f']:
        C=(eval(TempStr[0:-1])-32)/1.8
        c = "转换后的温度是{:.2f}C".format(C)
    elif TempStr[-1] in ['C','c']:
        F=1.8*eval(TempStr[0:-1])+32
        c = "转换后的温度是{:.2f}F".format(F)
    else:
        c = "输入格式有误"
    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,c) 

def show3():
    money = e4.get()
    if money[0:3] in ['RMB']:
        C=eval(money[3:])*17.519
        d = "USD{:.2f}".format(C)
    elif money[0:3] in ['USD']:
        F=eval(money[3:])/17.519
        d = "RMB{:.2f}".format(F)
    else:
        d = "输入格式有误"
    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,'\n')
    showarea.insert(INSERT,d)

def clear():
    showarea.delete(1.0,END)

 #创建控件
showarea = tk.Text(window,bg = 'palegreen',font = ('隶书',12),width = 38,height = 6,exportselection = True,relief = RAISED)

function1 = tk.Label(window,bg='lightcyan',width = 35,height = 5)
tip1 = tk.Label(function1,bg='lightcyan',text='身高：',font = ('楷体',12))
e1 = tk.Entry(function1,cursor = 'xterm',relief = SUNKEN)
m = tk.Label(function1,bg='lightcyan',text='米',font = ('楷体',12))
tip2 = tk.Label(function1,bg='lightcyan',text='体重：',font = ('楷体',12))
e2 = tk.Entry(function1,cursor = 'xterm',relief = SUNKEN)
kg = tk.Label(function1,bg='lightcyan',text='千克',font = ('楷体',12))
calculate1 = tk.Button(window,bg='honeydew',text='计算BMI',command = show1,relief = RAISED,font=('隶书',14))

function2 = tk.Label(window,bg='mistyrose',width = 35,height = 5)
tip3 = tk.Label(function2,bg='mistyrose',text='请输入带符号的温度值：',font = ('楷体',12))
e3 = tk.Entry(function2,cursor = 'xterm',relief = SUNKEN)
transform1 = tk.Button(window,bg='honeydew',text='温度转换',command = show2,relief = RAISED,font=('隶书',14))

function3 = tk.Label(window,bg='lavenderblush',width=35,height=5)
tip4 = tk.Label(function3,bg='lavenderblush',text='ARS/RMB转换',font=('黑体',14))
e4 = tk.Entry(function3,cursor='xterm',relief=SUNKEN)
transform2 = tk.Button(window,bg='honeydew',text='转换',command=show3,relief=RAISED,font=('隶书',14))


erase = tk.Button(window,bg='aliceblue',text='清空显示区',command = clear,relief = RAISED,font=('隶书',14))

 #放置控件
showarea.place(relx = 0.3,rely = 0.05)

function1.place(relx=0.01,rely=0.25)
tip1.place(relx = 0.01,rely = 0.2)
e1.place(relx = 0.25,rely = 0.2)
m.place(relx = 0.85,rely = 0.2)
tip2.place(relx = 0.01,rely = 0.6)
e2.place(relx = 0.25,rely = 0.6)
kg.place(relx = 0.85,rely = 0.6)
calculate1.place(relx = 0.123,rely = 0.405)

function2.place(relx = 0.34,rely = 0.25)
tip3.place(relx = 0.15,rely = 0.2)
e3.place(relx = 0.15,rely = 0.6)
transform1.place(relx = 0.43,rely = 0.405)

function3.place(relx = 0.67,rely = 0.25)
tip4.place(relx = 0.25,rely = 0.1)
e4.place(relx = 0.2,rely = 0.6)
transform2.place(relx = 0.785,rely = 0.405)


erase.place(relx = 0.75,rely = 0.1)

 #主窗口循环显示
window.mainloop()





