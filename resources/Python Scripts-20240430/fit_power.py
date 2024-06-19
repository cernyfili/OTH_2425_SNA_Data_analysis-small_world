## use a proper power law random number generator (or code your own) 
from networkx.utils import powerlaw_sequence
import powerlaw

#generate a random sequence from a power law with exponent 2.5 and check it powerlaw indentifies it
pl_sequence = powerlaw_sequence(10000,exponent=2.5)


data = pl_sequence
results = powerlaw.Fit(data)
print("alpha", results.power_law.alpha)
print("xmin",results.power_law.xmin)
print("signma",results.power_law.sigma)

#Check alternative
R, p = results.distribution_compare('power_law', 'lognormal')
print(R,p)

R, p = results.distribution_compare('power_law', 'exponential')
print(R,p)


