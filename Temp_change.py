import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation
import math

gridsize = 51

cmap = ListedColormap(['white', 'red', 'orange', 'yellow', 'yellowgreen', 'mediumblue', 'indigo'])

def get_user_float(message):
    try:
        output = float(input(message))
    except ValueError:
        return get_user_float()
    return output

def get_info():
    mass1 = get_user_float("mass of solution 1: ")
    temp1 = get_user_float("temperature of solution 1: ")

    mass2 = get_user_float("mass of solution 2: ")
    temp2 = get_user_float("temperature of solution 2: ")

    link = {temp1 : mass1,
            temp2 : mass2}

    check_temp = [temp1, temp2]
    max_t = max(check_temp)
    min_t = min(check_temp)

    set_info(max_t, min_t) #set intervals

    return link

def set_info(temp_max, temp_min):
    global temp_ranges

    range = temp_max - temp_min
    interval = range/6
    temp_ranges = [[0, interval], [interval + 1, 2*interval], [2*interval + 1, 3*interval], [3*interval + 1, 4*interval], [4*interval, + 1, 5*interval], [5*interval + 1, 6*interval]] #intervals as tubles: [0] = min, [1] = max




def temp_change():
    pass



def grid(size = gridsize):
    global temp_ranges

    Z = [[0 for x in range(size)] for x in range(size)]
    
    for x in range(1, len(temp_ranges)+1):
        print(x)
        Z[0][x] = x

    ax.set_xticks([])
    ax.set_yticks([])
    
    return Z

def grid_update():
    pass
    #if temp in first range (lowest temp), colour is cooler (blue/indigo) - if temp is last temp (highest temp), colour is warmer (red/orange)

def run(x):
    pass

get_info()

fig, ax = plt.subplots(figsize = (5,5))
image = ax.imshow(grid(), origin = 'upper', cmap=cmap)
ani = FuncAnimation(fig, run, frames = 100, interval = 100, blit = False)
plt.show()