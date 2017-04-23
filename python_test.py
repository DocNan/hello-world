# python code test
import numpy
import pylab


# -----------------------------------------------------------------------------
pylab.ion()

def draw_figures():
    pylab.figure()
    pylab.plot(numpy.array([1,2]),numpy.array([3,4]),'*',color='red')


draw_figures()
