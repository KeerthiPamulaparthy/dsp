[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

import nsfg
df = nsfg.ReadFemPreg()
pregordr = df['pregordr']
live = df[df.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
firsts.totalwgt_lb
others.totalwgt_lb
import math
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d 
CohenEffectSize(others.totalwgt_lb, firsts.totalwgt_lb)
firsts.prglngth
others.prglngth
CohenEffectSize(others.prglngth, firsts.prglngth)
"""Cohen's d communicates the variability within the groups. By comparing the total weight in lbs of the first babies and other babies, it appears that first babies are lighter than other babies. Comparing the pregnancy length, between first babies and other babies, it appears that first babies have a longer pregnancy length than other babies."""
