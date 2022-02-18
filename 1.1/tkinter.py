from tkinter import *
def calculation():
    try:
        num=int(a.get())
        num2=int(b.get())
        num3= num2+num
        c.set(str(num3))
        except ValueError:
            print("Пожалуйста, вводите только числа.")
windows=Tk()
windows.title("")
windows.geometry("400x400")

a=StringVar()
b=StringVar()
c=StringVar()


    
