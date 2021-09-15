import numpy as np
from matplotlib import pyplot as plt
import random
import matplotlib.cm as cm

def draw_polygon(ax):

    global x,y,n,center_point

    angles = np.arctan2(x-center_point[0],y-center_point[1])
    print(angles, " -углы")

    ## сортируем точки
    sort_tups = sorted([(i,j,k) for i,j,k in zip(x,y,angles)], key = lambda t: t[2])
    print(sort_tups, " -отсортированные точки")

    ## убеждаемся в отсутствии повторений
    if len(sort_tups) != len(set(sort_tups)):
        raise Exception('two equal coordinates -- exiting')

    x,y,angles = zip(*sort_tups)
    x = list(x)
    print(x, " -итоговые x")
    y = list(y)
    print(y, " -итоговые y")

    ## добавляем первый элемент в конец массива
    x.append(x[0])
    y.append(y[0])

    plt.ion()
    ax.plot(x,y,"magenta", label = '{}'.format(n))
    plt.draw()

    sq = [(center_point[0],center_point[1]),(center_point[0],center_point[1]+1),(center_point[0]+1,center_point[1]+1),(center_point[0]+1,center_point[1])]
    polygon_1 = plt.Polygon(sq, facecolor='r')
    ax.add_patch(polygon_1)
    #plt.scatter(center_point[0], center_point[1], color='magenta', s=100, marker='s')
    plt.draw()

    d = 1
    sq = [(center_point[0], center_point[1]), (center_point[0], center_point[1] + d),
          (center_point[0] + d, center_point[1] + d), (center_point[0] + d, center_point[1])]
    #for i in range(0, n-1, 1):

    print("End")
   # d = 0.1
    #fill_color(center_point[0]+d, center_point[1], d)
    #print("...")
    #fill_color(center_point[0]-d, center_point[1], d)
    #fill_color(center_point[0], center_point[1]+d, d)
    #fill_color(center_point[0], center_point[1]-d, d)


def fill_color(x0,y0,d):

    global x, y, n, center_point,x_list,y_list

    for i in range(0, n, 1):
        if (x[i] <= x[i + 1]):
            temp = 1
        else:
            temp = -1
        for j in range(x[i], x[i + 1], temp):
            if ((x0-x[i])/(x[i+1]-x[i])) != ((y0-y[i])/(y[i+1]-y[i])) and x_list.count(x0)==0 and y_list.count(y0)==0:
                plt.ion()
                plt.pause(0.1)
                plt.scatter(x0, y0, color='magenta', s=10, marker='s')
                plt.draw()
                fill_color(center_point[0] + d, center_point[1], d)

    x_list.append(x0)
    y_list.append(y0)



    ## определяем границы фигуры
    board_x = []
    board_y = []
    for i in range(0, n, 1):
        if (x[i] <= x[i + 1]):
            temp = 1
        else:
            temp = -1
        for j in range(x[i], x[i + 1], temp):
            board_x.append(j)
            board_y.append((((j - x[i]) / (x[i + 1] - x[i])) * (y[i + 1] - y[i])) + y[i])
    board_x.append(x[0])
    board_y.append(y[0])
        #if (center_point[0] + 0.1):
         #   plt.pause(2)
          #  plt.scatter(z_x, z_y, color='magenta', s=1, marker='o')
           # plt.draw()


## main
n = 4
x = np.random.randint(0, 50, n)
print(x, " -x")
y = np.random.randint(0, 50, n)
print(y, " -y")

## вычисляем центр полигона (это будет затравочным эдементом)
center_point = [np.sum(x)/n, np.sum(y)/n]
print(center_point, " -центр полигона")

x_list = []
y_list = []

fig,ax = plt.subplots()
draw_polygon(ax)

ax.legend()
plt.ioff()
plt.title("Закраска фигуры затравочным элементом", fontsize=14)
plt.show()