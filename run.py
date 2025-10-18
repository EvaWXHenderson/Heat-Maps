import heatmap_perlin as ht
import ColourSamplePerlin as cp 

def get_action():
    action = input('A: Sample colours for heatmap \n ' + 
                    'B: Generate heatmap')
    
    if action == 'A' or action == 'a':
        cp.run()

    if action == 'B' or action == 'b':
        ht.run()
    else:
        get_action()

get_action()