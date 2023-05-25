import random
import tkinter
import tkinter as tk
import time
from tkinter import *
import pandas as pd
from PIL import Image, ImageTk


def choose_topics():
    new_window = tk.Toplevel(window)
    new_window.title('Выбор тем')
    new_window.attributes('-fullscreen', True)
    widthN = new_window.winfo_screenwidth()
    heightN = new_window.winfo_screenheight()
    canvas2 = Canvas(new_window, width=widthN, height=heightN)
    canvas2.config(bg="#848470")
    canvas2.pack()
    canvas2.create_image(0, 0, image=img2, anchor="nw")
    new_window.geometry(f"{widthN}x{heightN}+0+0")

    animals = Button(new_window, text='ЖИВОТНЫЕ', command=interes, font='Arial 17', bg="#848470")
    animals.place(x=widthN - widthN/3.5, y=heightN - heightN/1.7)
    vegetables = Button(new_window, text='ОВОЩИ', command=interes2, font='Arial 17', bg="#848470")
    vegetables.place(x=widthN - widthN / 1.41, y=heightN - heightN / 5.2)
    colors = Button(new_window, text='ЦВЕТА', command=interes3, font='Arial 17', bg="#848470")
    colors.place(x=widthN - widthN / 1.25, y=heightN - heightN / 1.7)
    fruits = Button(new_window, text='ФРУКТЫ', command=interes1, font='Arial 17', bg="#848470")
    fruits.place(x=widthN - widthN /2.8, y=heightN - heightN/4.5)
    cities = Button(new_window, text='ГОРОДА', command=interes4, font='Arial 17', bg="#848470")
    cities.place(x=widthN - widthN /1.85, y=heightN - heightN/1.85)
    contButton = Button(new_window, text="CONTINUE", command=pred_start, font='Arial 17', bg="#848470")
    contButton.place(x=widthN - widthN/5.4, y=heightN - heightN/5)

def pred_start():
    winStart = tk.Toplevel(window)
    winStart.title('Name player')
    winStart.iconbitmap('иконка.ico')
    screen_width = winStart.winfo_screenwidth()
    screen_height = winStart.winfo_screenheight()
    win_width = 300
    win_height = 200
    winStart.resizable(width=False, height=False)
    x = (screen_width / 2) - (win_width / 2)
    y = (screen_height / 2) - (win_height / 2)
    winStart.configure(bg="#EEEEDF")
    winStart.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))
    name_label = tk.Label(winStart, text="Введите имя игрока:", font=("Arial", 14), bg="#848470")
    name_label.pack(pady=10)
    name_one = tk.Entry(winStart, font=("Arial", 14), width=20)
    name_one.pack()

    def save_name():
        global name1
        name1 = name_one.get()
        global player
        player = {"имя": name1, "количество": 0, "время": 1000000}

    button = Button(winStart, text='CONTINUE', bg="#848470", fg="black", command=lambda: [save_name(), start()],
                    font='Arial 18')
    button.pack(side="bottom", pady=20, padx=20)

def one():
    global count_player
    count_player = 1
def two():
    global count_player
    count_player = 2



def start():
    start_time = time.time()
    global lifes
    lifes = 5
    start_window = tk.Toplevel(window)
    start_window.attributes('-fullscreen', True)
    widthS = start_window.winfo_screenwidth()
    heightS = start_window.winfo_screenheight()
    start_window.title('Игра')
    canvas_start = Canvas(start_window, width=widthS, height=heightS)
    canvas_start.config(bg="#848470")
    canvas_start.pack()
    img_1 = Image.open("1.png")
    img_1 = img_1.resize((widthS, heightS), Image.LANCZOS)
    img_1 = ImageTk.PhotoImage(img_1)
    global bg_image1
    bg_image1 = img_1
    canvas_start.create_image(0, 0, image=img_1, anchor="nw")
    start_window.geometry(f"{width_window}x{height_window}+0+0")
    text = random.choice(slova)
    text1 = canvas_start.create_text(widthS / 2, heightS-620 ,
                              text="Вам выпала тема:"+str(text[0]),
                              font=("Arial", 25), fill="black")
    start_window.geometry(f"{widthS}x{heightS}+0+0")
    slovo_and_podskazka=random.choice(text[1::])
    slovo=slovo_and_podskazka[0]
    label_word=[]
    btn_alpha=[]
    def podskazka():
        window_podskazka = tk.Toplevel(window)
        window_podskazka.title('Подсказка')
        screen_width = window_podskazka.winfo_screenwidth()
        screen_height = window_podskazka.winfo_screenheight()
        win_width = 300
        win_height = 300
        window_podskazka.resizable(width=False, height=False)
        x = (screen_width / 2) - (win_width / 2)
        y = (screen_height / 2) - (win_height / 2)
        canvas = Canvas(window_podskazka, width=win_width, height=win_height)
        canvas.config(bg="#848470")
        canvas.pack()
        canvas.create_image(0, 0, image=img3, anchor="nw")
        canvas.create_text(150,260,text=slovo_and_podskazka[1], font='Arial 16')
        window_podskazka.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y))
        window_podskazka.iconbitmap('иконка.ico')


    def give_up():
        giveup = tk.Toplevel(window)
        giveup.title('Сдаться')

        button1 = tkinter.Button(giveup, text='Закончить игру', font='Arial 16', bg="#848470", command=close)
        button1.grid(row=1, column=0)

        button2 = tkinter.Button(giveup, text='Сменить слово', font='Arial 16', bg="#848470", command=start)
        button2.grid(row=1, column=1)

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
        button.place(x=800+x, y=350 -y)
        button = tkinter.Button(start_window, text='Сдаться', font='Arial 16',bg="#848470",command=give_up)
        button.place(x=980+x, y=350 -y)

    def pos_word(slovo):
        x = 0
        for i in range(len(slovo)):
            pos = Label(start_window, text='_', font='Arial 16',bg="#848470")
            pos.place(x=800+ x, y=270)
            x += 50
            label_word.append(pos)
    def draw():
        if lifes == 4:
            canvas_start.delete('all')
            img_z = Image.open("2.png")
            img_z = img_z.resize((widthS, heightS), Image.LANCZOS)
            img_z = ImageTk.PhotoImage(img_z)
            global bg_image
            bg_image = img_z
            canvas_start.create_image(0, 0, image=bg_image, anchor="nw")
            start_window.geometry(f"{widthS}x{heightS}+0+0")
        elif lifes == 3:
            canvas_start.delete('all')
            img_z = Image.open("3.png")
            img_z = img_z.resize((widthS, heightS), Image.LANCZOS)
            img_z = ImageTk.PhotoImage(img_z)
            global bg_image2
            bg_image2 = img_z
            canvas_start.create_image(0, 0, image=bg_image2, anchor="nw")
            start_window.geometry(f"{widthS}x{heightS}+0+0")
        elif lifes == 2:
            canvas_start.delete('all')
            img_z = Image.open("4.png")
            img_z = img_z.resize((widthS, heightS), Image.LANCZOS)
            img_z = ImageTk.PhotoImage(img_z)
            global bg_image3
            bg_image3 = img_z
            canvas_start.create_image(0, 0, image=bg_image3, anchor="nw")
            start_window.geometry(f"{widthS}x{heightS}+0+0")
        elif lifes == 1:
            canvas_start.delete('all')
            img_z = Image.open("5.png")
            img_z = img_z.resize((widthS, heightS), Image.LANCZOS)
            img_z = ImageTk.PhotoImage(img_z)
            global bg_image4
            bg_image4 = img_z
            canvas_start.create_image(0, 0, image=bg_image4, anchor="nw")
            start_window.geometry(f"{widthS}x{heightS}+0+0")
        else:
            canvas_start.delete('all')
            img_z = Image.open("6.png")
            img_z = img_z.resize((widthS, heightS), Image.LANCZOS)
            img_z = ImageTk.PhotoImage(img_z)
            global bg_image5
            bg_image5 = img_z
            canvas_start.create_image(0, 0, image=bg_image5, anchor="nw")
            start_window.geometry(f"{widthS}x{heightS}+0+0")
        text12 = canvas_start.create_text(widthS / 2, heightS - 620,
                                          text="Вам выпала тема:" + str(text[0]),
                                          font=("Arial", 25), fill="black")

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
        end_time = time.time()
        elapsed_time = end_time - start_time
        if status=='win':
            if (elapsed_time < player["время"]):
                player["время"] = elapsed_time
            player['количество'] +=1
            print(player)
            win = tk.Toplevel(window)
            win.title('Win')
            width_win = win.winfo_screenwidth()
            height_win = win.winfo_screenheight()
            canvas = Canvas(win, width=width_win, height=height_win)
            canvas.config(bg="#848470")
            canvas.pack()
            canvas.create_image(0, 0, image=img4, anchor="nw")
            button1 = Button(win, text='Закончить игру', font='Arial 16', bg="#848470", command=close)
            button1.place(x=width_win - width_win / 3.5, y=height_win - height_win / 1.7)
            button3 = tkinter.Button(win, text='Посмотреть рейтинг', font='Arial 16', bg="#848470")
            button3.place(x=width_win - width_win / 3.5, y=height_win - height_win / 2.2)
            button2 = tkinter.Button(win, text='Продолжить игру', font='Arial 16', bg="#848470", command=start)
            button2.place(x=width_win - width_win / 3.5, y=height_win - height_win / 3.2)
            win.geometry(f"{width_win}x{height_win}+0+0")
            win.attributes('-fullscreen', True)
        else:
            lose = tk.Toplevel(window)
            lose.title('Lose')
            width_lose = lose.winfo_screenwidth()
            height_lose = lose.winfo_screenheight()
            canvas = Canvas(lose, width=width_lose, height=height_lose)
            canvas.config(bg="#848470")
            canvas.pack()
            canvas.create_image(0, 0, image=img5, anchor="nw")
            button1 = Button(lose, text='Закончить игру', font='Arial 16', bg="#848470", command=close)
            button1.place(x=width_lose - width_lose / 3.5, y=height_lose - height_lose / 1.7)
            button3 = tkinter.Button(lose, text='Посмотреть рейтинг', font='Arial 16', bg="#848470")
            button3.place(x=width_lose - width_lose / 3.5, y=height_lose - height_lose / 2.2)
            button2 = tkinter.Button(lose, text='Продолжить игру', font='Arial 16', bg="#848470", command=start)
            button2.place(x=width_lose - width_lose / 3.5, y=height_lose - height_lose / 3.2)
            lose.geometry(f"{width_lose}x{height_lose}+0+0")
            lose.attributes('-fullscreen', True)

    alphabet()
    pos_word(slovo)

slova=[]
def interes():
    slova.append(["ЖИВОТНЫЕ",["ЗЕБРА","Место пешеходного перехода\n на проезжей части"],["ЖИРАФ","Самое высокое \nживотное суши"],["ГЕПАРД","Самое быстрое \nназемное животное"]])
def interes1():
    slova.append(["ФРУКТЫ",["ЯБЛОКО","Фрукт раздора \nгреческих богинь"],["ГРУША","Съедобная лампочка"],["БАНАН","Съедобный и длинный миньон"]])
def interes2():
    slova.append(["ОВОЩИ",["ПОМИДОР","Бычье сердце"],["ОГУРЕЦ","Овощ с желтыми цветами"],["КАПУСТА","Огородное растение \nс листьями"]])
def interes3():
    slova.append(["ЦВЕТА",["КРАСНЫЙ","Цвет крови"],["БЕЛЫЙ","Снег на улице ..."],["ЖЕЛТЫЙ","Подсолнух в огороде ..."]])
def interes4():
    slova.append(["ГОРОДА",["ТВЕРЬ","Город Кати Булыгиной"],["ПИТЕР","Город на болоте"],["МОСКВА","Столица России"]])
def close():
    with open('rating', 'w') as f:
        f.write(player.get("имя") + ' ')
        f.write(str(player.get("количество")) + ' ')
        f.write(str(player.get("время")) + '\n')
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
img=Image.open("игра виселица.png")
img = img.resize((width_window,height_window),Image.LANCZOS)
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor="nw")
window.geometry(f"{width_window}x{height_window}+0+0")

button = Button(window, text='START', bg="#848470",fg="black",command=choose_topics,font='Arial 20')
button.place(x=width_window-width_window/6, y=height_window-height_window/5)

img2 = Image.open("выбор_тем.png")
img2 = img2.resize((width_window, height_window), Image.LANCZOS)
img2 = ImageTk.PhotoImage(img2)

img3 = Image.open("podskazka.png")
img3 = img3.resize((300, 250), Image.LANCZOS)
img3 = ImageTk.PhotoImage(img3)

img4=Image.open("на окно win.png")
img4 = img4.resize((width_window, height_window), Image.LANCZOS)
img4 = ImageTk.PhotoImage(img4)

img5=Image.open("фон на проигрыш.png")
img5 = img5.resize((width_window, height_window), Image.LANCZOS)
img5 = ImageTk.PhotoImage(img5)


window.mainloop()