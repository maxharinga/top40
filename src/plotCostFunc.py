import pylab
import numpy

x = numpy.linspace(1,40,100) # 100 linearly spaced numbers
#y = numpy.exp(-(1*(x))/1)# computing the values of sin(x)/x
y = 2/(1 + numpy.exp(0.25*(x-1)))# computing the values of sin(x)/x



# compose plot
pylab.plot(x,y) 
pylab.show() 
