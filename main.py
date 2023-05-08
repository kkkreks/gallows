import random
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk


def choose_topics():
    new_window = tk.Toplevel(window)
    #new_window.geometry('1310x1000')
    new_window.state('zoomed')
    new_window.title('Выбор тем')
    #photo = tk.PhotoImage(file="png-clipart-cats-cats.png")
    #new_window.iconphoto(False, photo)
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
    label = Label(new_window, text="После выбора тем нажмите кнопку CONTINUE",font='Arial 17')
    label.pack()
    contButton = Button(new_window, text="CONTINUE",command=start,font='Arial 17')
    contButton.pack()


def start():
    start_window=tk.Toplevel(window)
    #start_window.geometry('1310x1000')
    start_window.state('zoomed')
    start_window.title('Игра')
    #photo = tk.PhotoImage(file="png-clipart-cats-cats.png")
    #start_window.iconphoto(False, photo)
    text=random.choice(slova)
    random_slovo = random.choice(slova[0])
    label = Label(start_window, text="Вам выпала тема: "+str(text[0]), font='Arial 17')
    label.pack()


    def split(random_slovo):
        return [char for char in random_slovo]

    split_slovo = split(random_slovo)
    split_slovo2 = split(random_slovo)

    print(random_slovo)
    s=[]
    def event_info():
        def klava(event):
            a = event.keysym

            if random_slovo.find(a) == -1:
                s.append("1")
                if len(s) == 1:
                    # голова
                    canvas.create_oval([450, 150], [550, 250], fill="pink", outline="yellow")
                if len(s) == 2:
                    # тело
                    canvas.create_polygon([500, 250], [400, 400], [600, 400], fill="pink", outline="yellow")
                if len(s) == 3:
                    # рука 1
                    canvas.create_line(450, 325, 500, 350, width=5, fill="#CD5C5C")
                if len(s) == 4:
                    # рука 2
                    canvas.create_line(550, 325, 500, 350, width=5, fill="#CD5C5C")
                if len(s) == 5:
                    # нога 1
                    canvas.create_line(475, 400, 475, 500, width=5, fill="#CD5C5C")
                if len(s) == 6:
                    # нога 2
                    canvas.create_line(525, 400, 525, 500, width=5, fill="#CD5C5C")
                if len(s) == 7:
                    # глаз 1
                    canvas.create_line(470, 170, 490, 190, width=2, fill="black")
                    canvas.create_line(490, 170, 470, 190, width=2, fill="black")
                    # глаз 2
                    canvas.create_line(510, 170, 530, 190, width=2, fill="black")
                    canvas.create_line(530, 170, 510, 190, width=2, fill="black")
                    game_over = Tk()
                    game_over.state('zoomed')
                    label = Label(game_over, text="game over", font='Arial 20')
                    label.pack(padx=10, pady=10)
                    if len(kate) > len(polina):
                        label = Label(game_over, text="выиграла kate", font='Arial 20')
                        label.pack(padx=20, pady=20)
                    else:
                        if len(kate) < len(polina):
                            label = Label(game_over, text="выиграла polina", font='Arial 20')
                            label.pack(padx=20, pady=20)
                        else:
                            label = Label(game_over, text="ничья", font='Arial 20')
                            label.pack(padx=20, pady=20)
            else:
                if len(hod) % 2 == 0:
                    kate.append("1")
                    canvas.create_text(900, 150, text=str(len(kate)), font="Verdana 19")
                    canvas.create_text(800, 150, text="KATE: ", font="Verdana 19", fill="red")
                    canvas.create_text(800, 200, text="POLINA: ", font="Verdana 19", fill="black")
                else:
                    polina.append("1")
                    canvas.create_text(900, 200, text=str(len(polina)), font="Verdana 19")
                    canvas.create_text(800, 150, text="KATE: ", font="Verdana 19", fill="black")
                    canvas.create_text(800, 200, text="POLINA: ", font="Verdana 19", fill="red")
                for i in range(0,len(split_slovo2)):
                    c=i*40
                    if split_slovo2[i]==a:
                        canvas.create_text(815 + c, 585, text=a, font="Verdana 19")
                    c=0

                for j in range(0,split_slovo.count(a)):
                    split_slovo.remove(a)
                if len(split_slovo)==0:
                    game_over = Tk()
                    game_over.state('zoomed')
                    label = Label(game_over, text="game over", font='Arial 20')
                    label.pack(padx=10, pady=10)
                    if len(kate)>len(polina):
                        label = Label(game_over, text="выиграла kate", font='Arial 20')
                        label.pack(padx=20, pady=20)
                    else:
                        if len(kate)<len(polina):
                            label = Label(game_over, text="выиграла polina", font='Arial 20')
                            label.pack(padx=20, pady=20)
                        else:
                            label = Label(game_over, text="ничья", font='Arial 20')
                            label.pack(padx=20, pady=20)

            hod.append("1")




        root = Tk()
        root.state('zoomed')

        canvas = Canvas(root, width=1200, height=1600, bg="gray", cursor="pencil")
        # висилица
        canvas.create_line(30, 10, 30, 1600, width=5, fill="black")
        canvas.create_line(30, 10, 500, 10, width=5, fill="black")
        canvas.create_line(500, 10, 500, 200, width=5, fill="black")

        canvas.create_text(800, 150, text="KATE: ", font="Verdana 19")
        canvas.create_text(800, 200, text="POLINA: ", font="Verdana 19")
        canvas.pack()

        kate=[]
        polina=[]
        hod=["1","1"]

        sum = 0
        for i in range(len(split_slovo)):
            canvas.create_line(800 + sum, 600, 830 + sum, 600, width=5, fill="black")
            sum += 40
        canvas.pack()


        root.bind('q', klava)
        root.bind('Q', klava)
        root.bind('w', klava)
        root.bind('W', klava)
        root.bind('e', klava)
        root.bind('E', klava)
        root.bind('r', klava)
        root.bind('R', klava)
        root.bind('t', klava)
        root.bind('T', klava)
        root.bind('y', klava)
        root.bind('Y', klava)
        root.bind('u', klava)
        root.bind('U', klava)
        root.bind('i', klava)
        root.bind('I', klava)
        root.bind('o', klava)
        root.bind('O', klava)
        root.bind('p', klava)
        root.bind('P', klava)
        root.bind('a', klava)
        root.bind('A', klava)
        root.bind('s', klava)
        root.bind('S', klava)
        root.bind('d', klava)
        root.bind('D', klava)
        root.bind('f', klava)
        root.bind('F', klava)
        root.bind('g', klava)
        root.bind('G', klava)
        root.bind('h', klava)
        root.bind('H', klava)
        root.bind('j', klava)
        root.bind('J', klava)
        root.bind('k', klava)
        root.bind('K', klava)
        root.bind('l', klava)
        root.bind('L', klava)
        root.bind('z', klava)
        root.bind('Z', klava)
        root.bind('x', klava)
        root.bind('X', klava)
        root.bind('c', klava)
        root.bind('C', klava)
        root.bind('v', klava)
        root.bind('V', klava)
        root.bind('b', klava)
        root.bind('B', klava)
        root.bind('n', klava)
        root.bind('N', klava)
        root.bind('m', klava)
        root.bind('M', klava)

    contButton = Button(start_window, text="CONTINUE", command=event_info, font='Arial 17')
    contButton.pack()


slova=[]
def interes():
    slova.append(["ANIMALS","zebra","cat","dog"])
def interes1():
    slova.append(["FRUITS","apple","pear","banana"])
def interes2():
    slova.append(["vegetables","tomato","cucumber","cabbage"])
def interes3():
    slova.append(["COLORS","red","white","black"])


window = Tk()
window.title('Игра виселица')
#window.geometry('1310x1000')
window.state('zoomed')
#photo=tk.PhotoImage(file="png-clipart-cats-cats.png")
#window.iconphoto(False,photo)

label = Label(window, text = "Добро пожаловать!",font='Arial 20')
label.pack(padx=10, pady=10)

label = Label(window, text = "Для начала игры нажмите кнопку START",font='Arial 20')
label.pack()
button = tkinter.Button(window, text='START', command=choose_topics,font='Arial 20')
button.pack()
label = Label(window, text = "Для начала игры нажмите кнопку START",font='Arial 20')
label.pack(padx=50,pady=50)


window.mainloop()




