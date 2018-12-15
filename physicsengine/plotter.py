from physicsengine.output import *
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle
cycol = cycle('bgrcmk')
class Plotter:
    def __init__(self, whatToPlot = Options.POSITION, timeToPlot=4000):
        self.timeToPlot = timeToPlot
        self.done = False
        self.bodiesInfo =  dict()
        self.option = whatToPlot

    def add_to_output(self, output):
        self.output = output
        output.plotter = self

    def plot(self):
       bodyIds = self.bodiesInfo.keys()
       option = self.option
       isVec = False
       i=1
       for b in bodyIds:
           print("ID: "+b)
           data=[]
           nArr=[]
           n=0
           bodyTimeAr = self.bodiesInfo[b]
           for bodyAtTime in bodyTimeAr:
               n+=1
               nArr.append(n)
               d = bodyAtTime[option]
               if isinstance(d, Vec2):
                   isVec = True
                   if len(data) == 0:
                       data.append([])
                       data.append([])
                   data[0].append(d.getX())
                   data[1].append(d.getY())
               else:
                   data.append(d)

           if len(data) > 0:
               if not isVec:
                    plt.plot(nArr, data, c=next(cycol), label='body {}'.format(b), linewidth=2)
                    plt.xlabel('Time')
                    plt.ylabel(option.value)

               else:
                   fig, (ax1, ax2) = plt.subplots(1, 2)
                   ax1.plot(nArr, data[0], c=next(cycol), label='body {}'.format(b), linewidth=2)
                   ax1.set_title(option.value + ".x")
                   ax1.set_xlabel('Time')
                   ax1.set_ylabel('x')
                   fig = plt.figure(i)
                   ax2.plot(nArr, data[1], c=next(cycol), label='body {}'.format(b), linewidth=2)
                   ax2.set_title(option.value + ".y")
                   ax2.set_xlabel('Time')
                   ax2.set_ylabel('y')
                   fig.canvas.set_window_title(option.value +" - body {}".format(b))
           i+=1





       #plt.legend()

       plt.show()



