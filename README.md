# Heat-Maps
## heatmap_perlin.py
Second attempt at a visual model/heat-map of heat diffusion between areas of differing temperature using Numpy, Matplotlib and Perlin Noise. Temperature changes occur based on an average of surrounding (top, bottom, left and right) temperatures.

Examples:
shape(2,2), dens = 50|shape(2,2), dens = 50|shape(4,4), dens = 25|shape(4,4), dens = 25
--|--|--|--
![](https://github.com/EvaWXHenderson/Heat-Maps/blob/main/media/Screen%20Recording%202025-10-12%20at%2017.09.25.gif)|![](https://github.com/EvaWXHenderson/Heat-Maps/blob/main/media/Screen%20Recording%202025-10-12%20at%2017.10.50.gif)|![](https://github.com/EvaWXHenderson/Heat-Maps/blob/main/media/Screen%20Recording%202025-10-12%20at%2017.11.31.gif)|![](https://github.com/EvaWXHenderson/Heat-Maps/blob/main/media/Screen%20Recording%202025-10-12%20at%2017.11.51.gif)
<p align="center">
Above: heatmap simulations of heat diffusion using different size of heat pockets specified by the parameters shape and dens >.
</p>

### Starting Visual Model
To generate a desired heat map simulation: size of heatpockets, simulation speed and colour scheme (see ColourSample.py) can be changed/chosen.

**Heat-pocket size:**    
Size of heat-pockets is controlled by parameters shape and dens taken by the pp.perlin() function:
for example:
```
perlin = np.abs(pp.perlin((4,4), dens=25)) #here shape = 4 and dens = 25
```
Increasing the shape parameter decreases heat-pocket size but increases heat-pocket frequency.     
Note that shape and dens must multiply to equal 100

**Simulation speed**    
Simulation speed can be controlled by the interval parameter taken by the FuncAnimation() function:
```
FuncAnimation(fig, run, frames = 100, interval = time per frame in ms, blit = False)
```

**Colour scheme:**    
next steps

(heatpockets on maps formed based Perlin Noise equations/packages)

## heatmap.py
Original attempt at a visual model/heat-map of the heat changes on mixing of 2 volumes of water of different temperatures using Numpy and Matplotlib (heatmap.py), where temperature changes occur based on taking new average temperatures of points above, below, left and right of each point. 

![](https://github.com/EvaWXHenderson/Heat-Maps/blob/main/media/Screen%20Recording%202025-10-08%20at%2020.52.35.gif)

### Starting Visual Model
To generate a desired heat map simulation: liquid temperatures and volumes, simulation speed, and colour scheme (see ColourSample.py) can be changed/chosen.

## Colour Sampler
ColourSample.py can be used to test colour themes/schemes for the heat map.

<p align="center">
  <img src="https://github.com/EvaWXHenderson/Heat-Maps/blob/main/media/cmapA.png" width="325" />
  <img src="https://github.com/EvaWXHenderson/Heat-Maps/blob/main/media/cmapD.png" width="325" /> 
  <img src="https://github.com/EvaWXHenderson/Heat-Maps/blob/main/media/cmapH.png" width="325" /> 
</p>
<p align="center">
Above: examples of heat map colour schemes A (left), D (centre) and H (right).
</p>
(sample maps formed based Perlin Noise equations/packages)


Current next steps:    
Integration of Colour sampler (ColourSample.py) and heatmap files to allow testing of colour schemes prior to running of heatmap visual.



## Sources:    
www.chemteam.info. (n.d.). The Final Temp after Mixing Two Amounts of Water. [online] Available at: https://www.chemteam.info/Thermochem/MixingWater.html.    

Alviar-Agnew, M. and Agnew, H. (2016). 3.12: Energy and Heat Capacity Calculations. [online] Chemistry LibreTexts. Available at: https://chem.libretexts.org/Bookshelves/Introductory_Chemistry/Introductory_Chemistry_(LibreTexts)/03%3A_Matter_and_Energy/3.12%3A_Energy_and_Heat_Capacity_Calculations.

Wikipedia. (2020). Perlin noise. [online] Available at: https://en.wikipedia.org/wiki/Perlin_noise.
