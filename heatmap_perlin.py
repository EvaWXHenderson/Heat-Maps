import matplotlib.pyplot as plt
import matplotlib.colors as pltcol
from matplotlib.animation import FuncAnimation

import pythonperlin as pp

import numpy as np


gridsize = 100

temp1 = 0
temp2 = 0

perlin = np.abs(pp.perlin((4,4), dens=25))
perlin[perlin > 0.5] = 0.5
#print(np.min(perlin),np.max(perlin))

heatmap = 200 + 200*(perlin*2)

colours255 = [(255, 255, 255),
              (98,161,219),
              (231,216,125),
              (221,159,64), 
              (180,69,31), 
              (176,17,17)] #white,blue,yellow,light-orange,orange,red
colours = []



def rgb_conversion(rgbvalues, new_rgb):

    for triple in rgbvalues:
        new_values = []
        for value in triple:
            new_value = value/255
            new_values.append(new_value)
    
        new_rgb.append(new_values)



def get_user_float(message):
    try:
        output = float(input(message))
    except ValueError:
        return get_user_float()
    return output
def get_info(info):
    global temp1, temp2, max_t, min_t

    if info == 'temp':
        temp1 = get_user_float("Input temperature of lowest point: ")

        temp2 = get_user_float("Input temperature of highest point: ")
    
    if info == 'min/max':
        check_temp = [temp1, temp2]
        max_t = max(check_temp)
        min_t = min(check_temp)

        set_info(max_t, min_t) #set intervals

        return max_t, min_t

def get_temp_click(event, index = heatmap):
    global ix, iy
    
    iy, ix= round(event.xdata), round(event.ydata)
    for x in range(100):
        for y in range(100):
            if x == ix and y == iy:
                temp = index[y,x]
                print('temp at ' + str((x, y)) + ": " + str(temp))
                return



def check_array(array = heatmap, v1=temp1, v2=temp2):
    v1count = 0
    v2count = 0

    for x in range(100):
        for y in range(100):
            if array[x,y] == v1:
                v1count +=1
            if array[x,y] == v2:
                v2count +=1
    print('tiles temp 1: ' + str(v1count))
    print('tiles temp 2: ' + str(v2count))
    print('total should add to 10,000: ' + str(v1count+v2count))
def check_maxmin(array): #for np array
    print(np.nanmax(array))
    print(np.nanmin(array))
def check_proportions(array):
    global gridsize, temp_ranges

    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0

    for x in range(gridsize):
        for y in range(gridsize):
            if array[x,y] >= temp_ranges[0][0] and array[x,y] <= temp_ranges[0][1] + 1:
                first += 1
            elif array[x,y] >= temp_ranges[1][0] and array[x,y] <= temp_ranges[1][1] + 1:
                second += 1
            elif array[x,y] >= temp_ranges[2][0] and array[x,y] <= temp_ranges[2][1] + 1:
                third += 1
            elif array[x,y] >= temp_ranges[3][0] and array[x,y] <= temp_ranges[3][1] + 1:
                fourth += 1
            elif array[x,y] >= temp_ranges[4][0] and array[x,y] <= temp_ranges[4][1] + 1:
                fifth += 1

    print('250-260: ' + str(first))
    print('260-270: ' + str(second))
    print('270-280: ' + str(third))
    print('280-290: ' + str(fourth))
    print('290-300: ' + str(fifth))



def initialise_grid(size = gridsize, tempgrid = heatmap):
    global temp1, temp2

    grid = [[0 for x in range(size)] for x in range(size)] #geneate 100x100 pixel display

    for x in range(size):
        for y in range(size):
            #print('temp needed: ' + str(tempgrid[x,y]))
            tile_colour = set_colour(tempgrid[x,y])
            grid[y][x] = tile_colour
    
    for x in range(0, len(temp_ranges)+1):
        grid[0][x] = x

    ax.set_xticks([])
    ax.set_yticks([])
        
    return grid



def set_start_info(info): #for testing
    global temp1, temp2, max_t, min_t

    if info == 'set':
        temp1 = 400
        temp2 = 200

        #print("mass1: " + str(mass1) + " temp1: " + str(temp1))
        #print("mass1: " + str(mass2) + " temp1: " + str(temp2))
    
    if info == 'min/max':
        check_temp = [temp1, temp2]
        max_t = max(check_temp)
        min_t = min(check_temp)

        set_info(max_t, min_t) #set intervals

        return max_t, min_t

def set_info(temp_max, temp_min, cmap = colours255):
    global temp_ranges

    total_range = temp_max - temp_min
    interval = total_range/(len(cmap)-1)
    
    temp_ranges = [[temp_min, temp_min+interval],[temp_min+interval+1, temp_min+2*interval],[temp_min+2*interval+1, temp_min+3*interval], [temp_min+3*interval+1, temp_min+4*interval], [temp_min+4*interval+1, temp_max]]
    #print("length: " + str(len(temp_ranges)) + " \n list: " + str(temp_ranges))

def set_colour(temp, cmap = colours255):
    global temp_ranges
    #print('temperature: ' + str(temp))
    colour = 0
    for x in range(len(temp_ranges)):
        #print('ranges: ' + str((int(temp_ranges[x][0]), int(temp_ranges[x][1])+1)))
        if temp >= temp_ranges[x][0] and temp <= temp_ranges[x][1] + 1:
            #print('in range: ' + str(temp_ranges[x]))
            colour = x+1
            #print("colour: " + str(colour) + "\n")
    
    return colour



def temp_change(temps, array = heatmap): #tempa has to be the tile changing
    total = 0

    for x in temps:
        total += x
    
    average = total/len(temps)
    
    return average #returns a temperature - asked for in Kelvin, mass in kg

def update_temps(array = heatmap):
    global gridsize
    done = False

    for x in range(gridsize-1):
        for y in range(gridsize-1):
            #tile = array[x,y]
            if x<=gridsize and y<=gridsize:
                surroundings = [array[x+1,y], array[x-1,y], array[x,y-1], array[x,y+1]]
            if x == 0:
                surroundings = [array[x+1,y], array[x,y], array[x,y-1], array[x,y+1]]
            #above, below, left, right
            array[x,y] = temp_change(temps = surroundings)

def update_grid(size = gridsize, tempgrid = heatmap):
    grid = [[0 for x in range(size+1)] for x in range(size+1)]
    
    for x in range(100):
        for y in range(100):
            tile_temp = tempgrid[x,y]
            tile_colour = set_colour(tile_temp)
            grid[y][x] = tile_colour
    
    return grid



def screen_run(x):
    ax.set_xticks([])
    ax.set_yticks([])

    update_temps()

    grid = update_grid()
    image.set_data(grid)



rgb_conversion(colours255, colours)
mapcolour = pltcol.LinearSegmentedColormap.from_list("", colours, N=len(colours))



get_info(info = 'temp')
set_start_info(info = 'min/max')
check_proportions(array = heatmap)
#set_heatmap()



fig, ax = plt.subplots(figsize = (5,5))
fig.canvas.mpl_connect('button_press_event', get_temp_click)

image = ax.imshow(initialise_grid(), origin = 'upper', cmap=mapcolour)
ani = FuncAnimation(fig, screen_run, frames = 100, interval = 125, blit = False)
plt.show()