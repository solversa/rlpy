######################################################
# Developed by Alborz Geramiard Dec 2nd 2012 at MIT #
######################################################
# Merge multiple results of several algorithms and show them on one plot

import sys, os
#Add all paths
path = '.'
while not os.path.exists(path+'/Tools.py'):
    path = path + '/..'
sys.path.insert(0, os.path.abspath(path))
from Tools import *

paths = ['.'] 
#paths = [
#        'Pendulum_InvertedBalance-IndependentDiscretization-20000',
#        'Pendulum_InvertedBalance-iFDD-20000-0.3'
#        ] 

colors      = ['b', 'g', 'r', 'c', 'm', 'y', 'k','purple']
styles      = ['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd']
MarkerSize  = 15
Legend      = True

merger = Merger(paths,colors = colors, styles= styles, markersize = MarkerSize, legend = Legend)
pl.ioff()
#print mergedData.means[0].shape
merger.plot('Return')
#merger.plot('Return','Time(s)')
#merger.plot('Steps')
#merger.plot('Steps','Learning Steps')
#merger.plot('Steps','Episodes')
#merger.plot('Steps','Time(s)')
#merger.plot('Steps','Time(s)')
#merger.plot('Features','Episodes')
#merger.plot('Terminal')
pl.show()


