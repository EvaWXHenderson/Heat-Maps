import heatmap_class as ht
import ColourSamplePerlin as cp 

def get_action():
    action = input('A: Sample colours for heatmap \n ' + 
                    'B: Generate heatmap')
    
    if action == 'A' or action == 'a':
        coloursampler = cp.ColourSampler()
        coloursampler.run()

        get_action()
        
    if action == 'B' or action == 'b':
        heatmap = ht.Heatmap()
        heatmap.run()
    else:
        get_action()

get_action()