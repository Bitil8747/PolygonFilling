from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from tkinter import *
import numpy as np
import random
import time

def draw():
    print("Начали!")
    global x, y, can

    for j in range(int(min(y)), int(max(y))):
        x_i = min(x)
        y_i = j
        i = 0
        for i in range(int(min(x)), int(max(x))):
            if ((i - x[0]) * (y[1] - y[0])) - ((y_i - y[0]) * (x[1] - x[0])) <= 0 \
                and ((i - x[1]) * (y[2] - y[1])) - ((y_i - y[1]) * (x[2] - x[1])) <= 0 \
                and ((i - x[2]) * (y[3] - y[2])) - ((y_i - y[2]) * (x[3] - x[2])) <= 0 \
                and ((i - x[3]) * (y[4] - y[3])) - ((y_i - y[3]) * (x[4] - x[3])) <= 0:
                can.create_rectangle(i, y_i, i + 1, y_i + 1, outline="#fcac00",
                                     fill="black")


def main():
    global x, y, n, can

    can.delete("all")

    x = np.random.randint(0, 50, n)
    print(x, " -x")
    y = np.random.randint(0, 50, n)
    print(y, " -y")

    x = list(x)
    y = list(y)
    x.sort()
    print(x, " -итоговые x")
    y.sort()
    print(y, " -итоговые y")
    tmp = x[n-1]
    x[n-1] = x[1]
    x[1] = tmp
    if x[1] > x[2]:
        tmp = x[2]
        x[2] = x[1]
        x[1] = tmp
    if y[1] > y[2]:
        tmp = y[2]
        y[2] = y[1]
        y[1] = tmp
    if ((x[1] - x[0]) * (y[2] - y[0])) - ((y[1] - y[0]) * (x[2] - x[0])) <= 0:
        y[1] = y[1] - ((y[1] - y[0]) / 2)
        x[1] = x[1] + ((x[2] - x[1]) / 2)
    if ((x[2] - x[1]) * (y[3] - y[1])) - ((y[2] - y[1]) * (x[3] - x[1])) <= 0:
        y[2] = y[2] + ((y[2] - y[1]) / 2)
        x[2] = x[2] + ((x[3] - x[2]) / 2)




    ## добавляем первый элемент в конец массива
    x.append(x[0])
    y.append(y[0])



    ## Рисуем многоугольник
    for i in range(0, n+1):
        x[i] = x[i] * 9 + 70
        y[i] = y[i] * 9 + 50
    for i in range(1,n+1):
        can.create_line(x[i-1],y[i-1],x[i],y[i], fill="#fcac00", width=2)
    can.pack()


    #can.bind('<Up>', draw())

    root.mainloop()


## Создаем рабочее окно для отрисовки
root = Tk()
root.title("Заполнение случайного многоугольника затравочным элементом")
root.geometry("800x600")
root.resizable(False, False)
can = Canvas(root, width=800, height=600, background="lightyellow")
button =Button(root, text="Закрасить",command=draw).place(x=350,y=550)
button2 =Button(root, text="Перестроить",command=main).place(x=450,y=550)
## Начальные данные
n = 4
x = np.random.randint(0, 50, n)
y = np.random.randint(0, 50, n)
main()
