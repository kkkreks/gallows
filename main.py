import random
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk


def choose_topics():
    new_window = tk.Toplevel(window)
    new_window.geometry('1310x1000')
    new_window.title('Выбор тем')
    photo = tk.PhotoImage(file="png-clipart-cats-cats.png")
    new_window.iconphoto(False, photo)
    label = Label(new_window, text="Выберите интересующие Вас темы:",font='Arial 17')
    label.pack()
    button = Button(new_window, text='ЖИВОТНЫЕ', command=interes,font='Arial 17')
    button.pack(padx=5, pady=5)
    button = Button(new_window, text='ФРУКТЫ', command=interes1,font='Arial 17')
    button.pack(padx=5, pady=5)
    button = Button(new_window, text='ОВОЩИ', command=interes2,font='Arial 17')
    button.pack(padx=5, pady=5)
    button = Button(new_window, text='ЦВЕТА', command=interes3,font='Arial 17')
    button.pack(padx=5, pady=5)
    button = Button(new_window, text='ГОРОДА', command=interes4,font='Arial 17')
    button.pack(padx=5, pady=5)
    label = Label(new_window, text="После выбора тем нажмите кнопку CONTINUE",font='Arial 17')
    label.pack()
    contButton = Button(new_window, text="CONTINUE",command=start,font='Arial 17')
    contButton.pack()

def start():
    start_window=tk.Toplevel(window)
    start_window.geometry('1310x1000')
    start_window.title('Игра')
    photo = tk.PhotoImage(file="png-clipart-cats-cats.png")
    start_window.iconphoto(False, photo)
    text=random.choice(slova)
    label = Label(start_window, text="Вам выпала тема:"+str(text[0]), font='Arial 17')
    label.pack()
    def alphabet():
        x = y = 0
        count = 0
        for c in range(ord('А'), ord('Я') + 1):
            button = Button(start_window,text=chr(c), font='Arial 16')
            button.place(x=800+x, y=350-y)
            x += 40
            count += 1
            if (count == 8):
                x = count = 0
                y -= 50
        button = tkinter.Button(start_window, text='Взять подсказку', font='Arial 16')
        button.place(x=800 +x, y=350 -y)
        button = tkinter.Button(start_window, text='Сдаться', font='Arial 16')
        button.place(x=800 +x+180, y=350 -y)


    alphabet()


slova=[]
def interes():
    slova.append(["ЖИВОТНЫЕ","зебра","кот","собака"])
def interes1():
    slova.append(["ФРУКТЫ","яблоко","груша","банан"])
def interes2():
    slova.append(["ОВОЩИ","помидор","огурец","капуста"])
def interes3():
    slova.append(["ЦВЕТА","красный","белый","желтый"])
def interes4():
    slova.append(["ГОРОДА","тверь","москва","томск"])

window = Tk()
window.title('Игра виселица')
window.geometry('1310x1000')
photo=tk.PhotoImage(file="png-clipart-cats-cats.png")
window.iconphoto(False,photo)

label = Label(window, text = "Добро пожаловать!",font='Arial 20')
label.pack(padx=10, pady=10)

label = Label(window, text = "Для начала игры нажмите кнопку START",font='Arial 20')
label.pack()
button = tkinter.Button(window, text='START', command=choose_topics,font='Arial 20')
button.pack()

'''canvas = Canvas(window, height=900, width=900)
canvas.place(x=100, y=200)
canvas.create_oval(100, 200, 140, 240)
canvas.create_line(120, 240, 120, 320)
canvas.create_line(120, 280, 120, 240)
canvas.create_line(120, 280, 160, 240)
canvas.create_line(120, 320, 80, 360)
canvas.create_line(120, 320, 160, 360)'''



'''button = tkinter.Button(frame, text='Выход', command=close_window)
button.pack()'''
window.mainloop()