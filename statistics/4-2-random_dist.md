[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)
import random
import thinkstats2
import thinkplot

rand_num = []
for i in range(1000):
    rand_num.append(random.random()) 
print rand_num

pmf = thinkstats2.Pmf(rand_num)
thinkplot.PrePlot(1)
thinkplot.Pmfs([pmf],linewidth=0.1)
thinkplot.Show(xlabel = 'frequency of numbers', ylabel = 'PMF')
cdf = thinkstats2.Cdf(rand_num)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='frequency of numbers', ylabel='CDF')
