import random
import tkinter
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


def choose_topics():
    new_window = tk.Toplevel(window)
    new_window.attributes('-fullscreen', True)
    widthN = new_window.winfo_screenwidth()
    heightN = new_window.winfo_screenheight()
    new_window.title('Выбор тем')
    canvas = Canvas(new_window, width=widthN, height=heightN)
    canvas.config(bg="#848470")
    canvas.pack()
    canvas.create_image(0, 0, image=img, anchor="nw")
    new_window.geometry(f"{widthN}x{heightN}+0+0")
    text1= canvas.create_text(width_window / 2 - 150, height_window / 2 - 270,
                              text="Выберите интересующие Вас темы:",
                              font=("Arial", 24), fill="white")
    animals = Button(new_window, text='ЖИВОТНЫЕ', command=interes,font='Arial 17',bg="#848470")
    animals.place(x=100, y=140)
    fruits = Button(new_window, text='ФРУКТЫ', command=interes1,font='Arial 17',bg="#848470")
    fruits.place(x=100, y=200)
    vegetables = Button(new_window, text='ОВОЩИ', command=interes2,font='Arial 17',bg="#848470")
    vegetables.place(x=100, y=260)
    colors = Button(new_window, text='ЦВЕТА', command=interes3,font='Arial 17',bg="#848470")
    colors.place(x=100, y=320)
    cities = Button(new_window, text='ГОРОДА', command=interes4,font='Arial 17',bg="#848470")
    cities.place(x=100, y=380)

    text = canvas.create_text(width_window / 2-150, height_window / 2+120,
                              text="Выберите тип игры:",
                              font=("Arial", 24), fill="white")

    contButton = Button(new_window, text="CONTINUE",command=pred_start,font='Arial 17',bg="#848470")
    contButton.place(x=widthN-250,y=heightN-150)

    oneplayer = Button(new_window, text="1 ИГРОК",command=one,font='Arial 17', bg="#848470")
    oneplayer.place(x=170, y=550)

    twoplayer = Button(new_window, text="2 ИГРОКА",command=two, font='Arial 17', bg="#848470")
    twoplayer.place(x=350, y=550)
count_player=0
def vbr_game():
    if count_player==1:
        start()
    else:
        'тут сделать функцию для игры на двух человек'
def pred_start():
    winStart = tk.Toplevel(window)
    winStart.title('Имена игроков')
    screen_width = winStart.winfo_screenwidth()
    screen_height = winStart.winfo_screenheight()
    win_width = 300
    win_height = 180
    x = (screen_width / 2) - (win_width / 2)
    y = (screen_height / 2) - (win_height / 2)
    winStart.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))
    if count_player==1:
        label = Label(winStart, text="Введите имя игрока:", font='Arial 18')
        label.pack()
        frame1 = tkinter.Frame(winStart)
        frame1.pack()
        name_one = tkinter.Entry(frame1)
        name_one.pack()
        name1 = name_one.get()
        button = Button(winStart, text='CONTINUE', bg="#848470", fg="black", command=start, font='Arial 18')
        button.place(x=win_width - 150, y=win_height - 40)
    elif count_player==2:
        label = Label(winStart, text="Введите имена игроков", font='Arial 18',bg="#848470")
        label.pack()
        label = Label(winStart, text="Имя первого игрока:", font='Arial 18')
        label.pack()
        frame1 = tkinter.Frame(winStart)
        frame1.pack()
        name_one = tkinter.Entry(frame1)
        name_one.pack()
        name1 = name_one.get()
        label = Label(winStart, text="Имя второго игрока:", font='Arial 18')
        label.pack()
        frame2 = tkinter.Frame(winStart)
        frame2.pack()
        name_two = tkinter.Entry(frame2)
        name_two.pack()
        name2 = name_two.get()
        button = Button(winStart, text='CONTINUE', bg="#848470", fg="black", command=vbr_game, font='Arial 18')
        button.place(x=win_width-150, y=win_height-40)
    else:
        label = Label(winStart, text="Выберите количество\n"
                                     "игроков", font='Arial 18')
        label.pack()

def one():
    global count_player
    count_player = 1
def two():
    global count_player
    count_player = 2



def start():
    global lifes
    lifes=5
    start_window=tk.Toplevel(window)
    start_window.attributes('-fullscreen', True)
    widthS = start_window.winfo_screenwidth()
    heightS = start_window.winfo_screenheight()
    start_window.title('Игра')
    canvas = Canvas(start_window, width=widthS, height=heightS)
    canvas.config(bg="#848470")
    canvas.pack()
    canvas.create_image(0, 0, image=img, anchor="nw")
    start_window.geometry(f"{width_window}x{height_window}+0+0")
    text=random.choice(slova)
    text1 = canvas.create_text(widthS / 2, heightS-620 ,
                              text="Вам выпала тема:"+str(text[0]),
                              font=("Arial", 20), fill="white")
    slovo_and_podskazka=random.choice(text[1::])
    slovo=slovo_and_podskazka[0]
    label_word=[]
    btn_alpha=[]
    def podskazka():
        window_podskazka = tk.Toplevel(window)
        window_podskazka.title('Подсказка')
        label = Label(window_podskazka, text=slovo_and_podskazka[1], font='Arial 16',bg="#848470")
        label.pack()
    def alphabet():
        x = y = 0
        count = 0
        for c in range(ord('А'), ord('Я') + 1):
            button = Button(start_window,text=chr(c), font='Arial 16',bg="#848470")
            button.place(x=800+x, y=350-y)
            button.bind('<Button-1>', lambda clicking: check(clicking,slovo))
            btn_alpha.append(button)
            x += 40
            count += 1
            if (count == 8):
                x = count = 0
                y -= 50
        button = tkinter.Button(start_window, text='Взять подсказку', font='Arial 16',bg="#848470",command=podskazka)
        button.place(x=800 +x, y=350 -y)
        button = tkinter.Button(start_window, text='Сдаться', font='Arial 16',bg="#848470")
        button.place(x=800 +x+180, y=350 -y)

    def pos_word(slovo):
        x = 0
        for i in range(len(slovo)):
            pos = Label(start_window, text='_', font='Arial 16',bg="#848470")
            pos.place(x=800+ x, y=270)
            x += 50
            label_word.append(pos)
    def draw():
        if lifes==4:
            'либо рисовать человечка либо менять фон с частями виселицы'
        elif lifes==3:
            1
        elif lifes==2:
            1
        elif lifes==1:
            1
        else:
            1

    def check(clicking, slovo):
        alpha = clicking.widget['text']
        pos = []
        for i in range(len(slovo)):
            if (slovo[i] == alpha):
                pos.append(i)
                for btn in btn_alpha:
                    if btn["text"] == alpha:
                        btn["bg"] = "green"
        if (pos):
            for i in pos:
                label_word[i].config(text='{}'.format(slovo[i]))
            count_alpha=0
            for i in label_word:
                if(i["text"].isalpha()):
                    count_alpha+=1
            if (count_alpha==len(slovo)):
                game_over('win')
        else:
            global lifes
            lifes-=1
            draw()
            for btn in btn_alpha:
                if btn["text"] == alpha:
                    btn["bg"] = "red"
            if (lifes==0):
                game_over('lose')
    def game_over(status):
        if status=='win':
            print('win')
        else:
            print('lose')
            '''доделать окна с вариантами что делать дальше'''

    alphabet()
    pos_word(slovo)



slova=[]
def interes():
    slova.append(["ЖИВОТНЫЕ",["ЗЕБРА","Место пешеходного перехода на проезжей части"],["ЖИРАФ","Самое высокое животное суши"],["ГЕПАРД","Самое быстрое наземное животное"]])
def interes1():
    slova.append(["ФРУКТЫ","ЯБЛОКО","ГРУША","БАНАН"])
def interes2():
    slova.append(["ОВОЩИ","ПОМИДОР","ОГУРЕЦ","КАПУСТА"])
def interes3():
    slova.append(["ЦВЕТА","КРАСНЫЙ","БЕЛЫЙ","ЖЕЛТЫЙ"])
def interes4():
    slova.append(["ГОРОДА","ТВЕРЬ","МОСКВА","ТОМСК"])
def close():
    window.destroy()



def close_window():
    window1 = tk.Toplevel(window)
    window1.title('Закрыть игру')
    label = Label(window1, text="Вы уверены что хотите покинуть игру?", font='Arial 20')
    label.pack()
    button = Button(window1, text='ДА', command=close, font='Arial 20')
    button.pack()
    button = Button(window1, text='НЕТ', font='Arial 20')
    button.pack()

"Создание главного окна"
window = Tk()
window.title ("Игра виселица")
window.attributes('-fullscreen', True)

width_window=window.winfo_screenwidth()
height_window=window.winfo_screenheight()

canvas=Canvas(window,width=width_window,height=height_window)
canvas.config(bg="#848470")
canvas.pack()
img=Image.open("imgonline-com-ua-Resize-bmg6Ur2mJa.png")
img = img.resize((width_window,height_window),Image.LANCZOS)
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor="nw")
window.geometry(f"{width_window}x{height_window}+0+0")

text = canvas.create_text(width_window/2, height_window/2, text="Добро пожаловать в игру Виселица!\n"
                                                                "Ознакомьтесь с правилами игры и нажмите кнопку START", font=("Arial", 24), fill="white", anchor="center")

button = Button(window, text='START', bg="#848470",fg="black",command=choose_topics,font='Arial 20')
button.place(x=width_window-200, y=height_window-135)

window.mainloop()