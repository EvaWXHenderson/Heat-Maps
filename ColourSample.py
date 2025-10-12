import matplotlib.pyplot as plt
import matplotlib.colors as pltcol

import pythonperlin as pp

import random as rand

colours1 = []
grid = []

#colours to go in order: white, warmest - coolest
Colourmaps_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Colourmaps_lists = [[(255, 255, 255), (176,17,17), (180,69,31), (221,159,64), (231,216,125), (98,161,219)],
                    [(255, 255, 255),(233,62,58),(237,104,60), (243,144,63), (253,199,12),(255,243,59)],
                    [(255, 255, 255),(155,147,174),(163,157,184),(197,191,212),(208,199,221),(211,209,221)],
                    [(255, 255, 255),(238,62,50),(246,136,56),(251,176,33),(27,138,90),(29,72,119)],
                    [(255, 255, 255),(95,85,90),(0,84,77),(117,156,138),(203,219,205),(223,216,210)],
                    [(255, 255, 255),(180,54,0),(189,67,0),(221,45,0),(234,61,3),(255,77,0)],
                    [(255, 255, 255),(255,0,0),(249,48,48),(244,76,76),(244,109,109),(249,144,144)]]

def get_gridsize():
    str_gridsize = input("Input integer value for grid size (i.e. integer x by x grid) \n")
    gridsize = int(str_gridsize)

    return gridsize
def get_colours():
    Colourmap_key = input("Input value code for desired colour set to try \n")
    for x in range(len(Colourmaps_names)):
        if Colourmaps_names[x] == Colourmap_key:
            Colour_list = x
    Colourmap_value = Colourmaps_lists[Colour_list] #list of colours

    return Colourmap_value
def rgb_conversion(rgbvalues, new_rgb):

    for triple in rgbvalues:
        new_values = []
        for value in triple:
            new_value = value/255
            new_values.append(new_value)
    
        new_rgb.append(new_values)
def set_colours(clist = colours1):
    colours = pltcol.LinearSegmentedColormap.from_list("", clist, N=len(clist)) 
    return colours

def input_task():
    task = input('Would you like to test another palette (A) or go on to heatmap generator (B)?')
    if task == 'A' or task == 'a':
        task_chosen = ''
    elif task == 'B' or task == 'b':
       task_chosen = ''
    else:
        input_task()

    return task_chosen
def output_task():
    pass
    """if task = test again ---> call function to run colour test again
        if task = move on ---> call heat map file """

#put below into run function:
gridsize = get_gridsize()
colours_255 = get_colours()
rgb_conversion(rgbvalues=colours_255, new_rgb=colours1)
colours = set_colours()


def set_grid(size = gridsize, cmap = colours_255):
    grid = [[0 for x in range(size)] for x in range(size)] 

    def reset_colour():
        colour = rand.randint(1, len(cmap))
        #print(colour)
        grid[y][x] = colour

    for x in range(size):
        for y in range(size):
            reset_colour()
    
    grid[0][0] = 0
        
    ax.set_xticks([])
    ax.set_yticks([])

    return grid


fig, ax = plt.subplots(figsize = (5,5))
image = ax.imshow(set_grid(), origin = 'upper', cmap=colours)
plt.show()