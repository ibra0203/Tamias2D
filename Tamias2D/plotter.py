from Tamias2D.output import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import math
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

    def _to_curve(self, ar, lastN):
        curve = []
        T = np.array([])
        if (isinstance(ar[0], list)):
            x = np.array(ar[0])
            y = np.array(ar[1])
            fX = interp1d(np.arange(len(x)), x, kind="quadratic")
            fY = interp1d(np.arange(len(y)), y, kind="quadratic")
            tnew = np.arange(0, len(x)-1, 0.1)
            xnew = fX(tnew)
            curve.append(xnew)
            ynew = fY(tnew)

            T= np.linspace(0, lastN, len(xnew))
            curve.append(ynew)

        else:
            x=5
        return curve, T

    def plot(self):
       bodyIds = self.bodiesInfo.keys()
       option = self.option
       isVec = False
       i=1
       nArr =[]
       for b in bodyIds:
           print("ID: "+b)
           data=[]
           lastN=0
           bodyTimeAr = self.bodiesInfo[b]
           for bodyAtTime in bodyTimeAr:
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
               thisN = bodyAtTime['n']
               nArr.append(thisN)
               lastN = math.floor(thisN)
           if len(data) > 0:
               curve, T = self._to_curve(data, lastN)
               if not isVec:
                    plt.plot(T, curve, c=next(cycol), label='body {}'.format(b), linewidth=2)
                    plt.xlabel('Time')
                    plt.ylabel(option.value)

               else:
                   fig, (ax1, ax2) = plt.subplots(1, 2)
                   ax1.plot(T, curve[0], c=next(cycol), label='body {}'.format(b), linewidth=2)
                   ax1.set_title(option.value + ".x")
                   ax1.set_xlabel('Time')
                   ax1.set_ylabel('x')
                   fig = plt.figure(i)
                   ax2.plot(T, curve[1], c=next(cycol), label='body {}'.format(b), linewidth=2)
                   ax2.set_title(option.value + ".y")
                   ax2.set_xlabel('Time')
                   ax2.set_ylabel('y')
                   fig.canvas.set_window_title(option.value +" - body {}".format(b))
           i+=1





       #plt.legend()

       plt.show()



