import pythonperlin as pp

import matplotlib.colors as pltcol
import matplotlib.pyplot as plt

colours1 = []

#colours to go in order: white, warmest - coolest
Colourmaps_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
Colourmaps_lists = [[(176,17,17), (180,69,31), (221,159,64), (231,216,125), (98,161,219)],
                    [(233,62,58),(237,104,60), (243,144,63), (253,199,12),(255,243,59)],
                    [(155,147,174),(163,157,184),(197,191,212),(208,199,221),(211,209,221)],
                    [(238,62,50),(246,136,56),(251,176,33),(27,138,90),(29,72,119)],
                    [(95,85,90),(0,84,77),(117,156,138),(203,219,205),(223,216,210)],
                    [(180,54,0),(189,67,0),(221,45,0),(234,61,3),(255,77,0)],
                    [(255,0,0),(249,48,48),(244,76,76),(244,109,109),(249,144,144)],
                    [(68,1,84), (59,82,139), (33,145,140), (94,201, 98), (253,231,37)],
                    [(179, 46, 95),(194, 78, 125),(0, 33, 140),(51, 93, 190),(44, 183, 209),(70, 208, 219)]]



def get_colours():
    Colourmap_key = input("Input value code for desired colour set to try \n")
    for x in range(len(Colourmaps_names)):
        if Colourmaps_names[x] == Colourmap_key:
            Colour_list = x
    Colourmap_value = Colourmaps_lists[Colour_list] #list of colours

    return Colourmap_value
def set_colours(clist = colours1):
    colours = pltcol.LinearSegmentedColormap.from_list("", clist, N=len(clist)+3) 
    return colours
def rgb_conversion(rgbvalues, new_rgb):

    for triple in rgbvalues:
        new_values = []
        for value in triple:
            new_value = value/255
            new_values.append(new_value)
    
        new_rgb.append(new_values)


def input_task():
    task = input('Would you like to test another palette (A) or go on to heatmap generator (B)?')
    if task == 'A' or task == 'a':
        task_chosen = ''
    elif task == 'B' or task == 'b':
       task_chosen = ''
    else:
        input_task()

    return task_chosen
def output_task(input):
    pass
    if input == 'A':
        get_colours()
    elif input == 'B':

    

colours_255 = get_colours()
rgb_conversion(rgbvalues=colours_255, new_rgb=colours1)
colours = set_colours()


dens = 65
shape = (8,8)
x = pp.perlin(shape, dens=dens)

#ax.set_xticks([])
#ax.set_yticks([])

fig, ax = plt.subplots(1,1)
ax.imshow(x, cmap = colours)
ax.set_xticks([])
ax.set_yticks([])

plt.show()

output_task(input = input_task())