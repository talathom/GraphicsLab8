import viz
import vizshape
import vizcam
import random
import math

from terrainLab import *

			
# Driver for terrain program			
viz.window.setSize( 640*2, 480*2 )
viz.window.setName( "Greys River, WY" )
window = viz.MainWindow
viz.MainWindow.clearcolor( viz.BLACK ) 

# create terrain
Terrain()

vizcam.PivotNavigate(center=[100,2000,100],distance=300)

# start rendering scene in the window
viz.go()
