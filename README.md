# Heat-Maps
A visual model/heat map of the heat changes on mixing of 2 volumes of water of different temperatures using Numpy and Matplotlib (heatmap.py).

Temperature changes occur based on taking new average temperatures of points above, below, left and right of each point. 

To generate a desired heat map simulation: resolution/dimensions and colour scheme (see ColourSample.py) can be changed/chosen.

![](https://github.com/EvaWXHenderson/Heat-Maps/blob/main/Screen%20Recording%202025-10-08%20at%2020.52.35.gif)

<!--Final temperatures are found using the following logic/equations (where Q is heat transfer in system and C<sub>p</sub> is the specific heat capacity under constant pressure):

 <p align="center">
$Q = (mass)(ΔT)(C_{p})$
</p>
<p align="center">
$Q_{lost} = Q_{gain}$
</p>
<p align="center">
$(mass_{a}*(T_{a} - T_{final})) (C_{p}) = (mass_{b}*(T_{b} - T_{final})) (C_{p})$
</p> -->

Current next steps:    
looking into Navier-Stokes equation to try make the movement of heat/diffusion look more realisitic.

## Colour Sampler
ColourSample.py can be used to test colour themes/schemes for the heat map, some set colour schemes to choose from:

'insert samples'

(sample maps formed based Perlin Noise equations/packages)

## Sources:    
www.chemteam.info. (n.d.). The Final Temp after Mixing Two Amounts of Water. [online] Available at: https://www.chemteam.info/Thermochem/MixingWater.html.    

Alviar-Agnew, M. and Agnew, H. (2016). 3.12: Energy and Heat Capacity Calculations. [online] Chemistry LibreTexts. Available at: https://chem.libretexts.org/Bookshelves/Introductory_Chemistry/Introductory_Chemistry_(LibreTexts)/03%3A_Matter_and_Energy/3.12%3A_Energy_and_Heat_Capacity_Calculations.

Wikipedia. (2020). Perlin noise. [online] Available at: https://en.wikipedia.org/wiki/Perlin_noise.
