import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation
import numpy as np

gridsize = 100
heatmap = np.array(gridsize,gridsize)
cmap = ListedColormap(['white', 'navy', 'mediumblue', 'yellowgreen', 'yellow','orange', 'red'])

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



def set_info(temp_max, temp_min):
    global temp_ranges

    range = temp_max - temp_min
    interval = range/6
    temp_ranges = [[temp_min, temp_min + interval], 
                   [temp_min + interval + 1, temp_min + 2*interval], 
                   [temp_min + 2*interval + 1, temp_min + 3*interval], 
                   [temp_min + 3*interval + 1, temp_min + 4*interval], 
                   [temp_min + 4*interval, + 1,temp_min + 5*interval], 
                   [temp_min + 5*interval + 1, temp_min + 6*interval]]

def set_colour(temp):
    global temp_ranges
    
    for x in range(len(temp_ranges)):
        if temp in range(int(temp_ranges[x][0]), int(temp_ranges[x][1])+1):
            colour = x+2
            print(str(temp) + " " + str((int(temp_ranges[x][0]), int(temp_ranges[x][1])+1)) + " " + str(colour))
    
    return colour

def set_proportions():
    global mass1, mass2, temp1, temp2

    portion1 = mass1/(mass1+mass2) #should get a decimal proportion

    tiles1 = portion1*100
    tiles2 = 100 - tiles1

    #print(tiles1, tiles2)

    return tiles1, tiles2



def temp_change():
    global mass1, mass2, temp1, temp2

    X = ((mass2*temp2) - (mass1*temp1))/(mass2-mass1)

    return X #returns a temperature - asked for in Kelvin, mass in kg



def initialise_grid(size = gridsize):
    global temp1, temp2

    grid = [[0 for x in range(size+1)] for x in range(size+1)] #geneate 100x100 pixel display

    tiles1, tiles2 = set_proportions()
    set1 = int(tiles1)

    colour1 = set_colour(temp1)
    colour2 = set_colour(temp2)

    print(str(temp1) + " " + str(colour1))
    print(str(temp2) + " " + str(colour2))
    
    for x in range(0, set1):
        for y in range(size):
            grid[y][x] = colour1
            #print([x, y], Z[y][x])
    
    for a in range(set1, size):
        for b in range(size):
            grid[b][a] = colour2
            #print([a, b], Z[b][a])
    
    for x in range(1, len(temp_ranges)+1):
        grid[0][x] = x

    ax.set_xticks([])
    ax.set_yticks([])
        
    return grid

def grid_update(size = gridsize, tempgrid = heatmap):
    grid = [[0 for x in range(size+1)] for x in range(size+1)]
    
    for x in range(100):
        for y in range(100):
            tile_temp = tempgrid[x][y]
            tile_colour = set_colour(tile_temp)
            grid[y][x] = tile_colour
    
    return grid

    #update np array and Z array
    #if temp in first range (lowest temp), colour is cooler (blue/indigo) - if temp is last temp (highest temp), colour is warmer (red/orange)

def run(x):
    pass



get_info(info = 'set')
get_info(info = 'min/max')



fig, ax = plt.subplots(figsize = (5,5))
image = ax.imshow(initialise_grid(), origin = 'upper', cmap=cmap)
ani = FuncAnimation(fig, run, frames = 100, interval = 100, blit = False)
plt.show()