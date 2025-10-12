import matplotlib.pyplot as plt
import matplotlib.colors as pltcol
from matplotlib.animation import FuncAnimation

import numpy as np


gridsize = 100

mass1 = 0
mass2 = 0

temp1 = 0
temp2 = 0

heatmap = np.zeros((100,100))

colours255 = [(255, 255, 255), 
            (176,17,17), 
            (180,69,31), 
            (221,159,64), 
            (231,216,125), 
            (98,161,219)] #white, red, orange, light-orange, yellow, blue
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
    global mass1, mass2, temp1, temp2, max_t, min_t

    if info == 'set':
        mass1 = get_user_float("mass of solution 1 (kg): ")
        temp1 = get_user_float("temperature of solution 1 (K): ")

        mass2 = get_user_float("mass of solution 2(kg): ")
        temp2 = get_user_float("temperature of solution 2 (K): ")
    
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
                temp = index[x,y]
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
    global mass1, mass2, temp1, temp2, max_t, min_t

    if info == 'set':
        mass1 = 100
        temp1 = 300

        mass2 = 60
        temp2 = 250

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

    for x in range(len(temp_ranges)):
        #print('ranges: ' + str((int(temp_ranges[x][0]), int(temp_ranges[x][1])+1)))
        if temp >= temp_ranges[x][0] and temp <= temp_ranges[x][1] + 1:
            #print('in range: ' + str(temp_ranges[x]))
            colour = x+1
            #print("colour: " + str(colour) + "\n")
    
    return colour

def set_proportions():
    global mass1, mass2, temp1, temp2

    portion1 = mass1/(mass1+mass2) #should get a decimal proportion

    tiles1 = portion1*100
    tiles2 = 100 - tiles1

    #print(tiles1, tiles2)

    return tiles1, tiles2

def set_heatmap(size = gridsize, tempgrid = heatmap):
    global temp1, temp2

    tiles1, tiles2 = set_proportions()
    set1 = int(tiles1)

    colour1 = set_colour(temp1)
    colour2 = set_colour(temp2)

    for x in range(0, set1):
        for y in range(size):
            tempgrid[x,y] = temp1
    for x in range(set1, size):
        for y in range(size):
            tempgrid[x,y] = temp2

    #check_array()
    #print(heatmap)



def temp_change(temps, array = heatmap): #tempa has to be the tile changing
    total = 0

    for x in temps:
        total += x
    
    average = total/len(temps)
    
    return average #returns a temperature - asked for in Kelvin, mass in kg

def update_temps(array = heatmap, gridsize = 100):
    done = False

    for x in range(gridsize-1):
        for y in range(gridsize-1):
            #tile = array[x,y]
            if x<=100 and y<=100:
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



def run(x):
    ax.set_xticks([])
    ax.set_yticks([])

    update_temps()

    grid = update_grid()
    image.set_data(grid)

def heatmap_run():
    rgb_conversion(colours255, colours)
    mapcolour = pltcol.LinearSegmentedColormap.from_list("", colours, N=len(colours))

    set_start_info(info = 'set')
    set_start_info(info = 'min/max')
    set_heatmap()



    fig, ax = plt.subplots(figsize = (5,5))
    fig.canvas.mpl_connect('button_press_event', get_temp_click)

    image = ax.imshow(initialise_grid(), origin = 'upper', cmap=mapcolour)
    ani = FuncAnimation(fig, run, frames = 100, interval = 100, blit = False)
    plt.show()

    check_maxmin(heatmap)