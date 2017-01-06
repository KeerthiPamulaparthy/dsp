[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)
dist.mean(), dist.std()
dist.cdf(mu-sigma)
def height_conversion(ft,cm):
    ht_cm = ft*30.48+cm*2.54
    return ht_cm
h1 = height_conversion(5,10)
h2 = height_conversion(6,1)
low = dist.cdf(h1)
high = dist.cdf(h2)
high - low
