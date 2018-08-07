'''
Created on 6 Aug 2018

@author: benos
'''
from __future__ import print_function
import openturns as ot
from openturns.viewer import View

graph = ot.Normal().drawPDF()
view = View(graph, plot_kwargs={'color':'blue'})
view.save('curve.png', dpi=100)
view.show()
i = 2