from scipy.stats import multinomial
import numpy as np
import sys

np.random.seed(0)

query = int(sys.argv[1]) if len(sys.argv) > 1 else 3
trials = int(sys.argv[2]) if len(sys.argv) > 2 else 1
sides = int(sys.argv[3]) if len(sys.argv) > 3 else 6
die = np.array(range(1, sides+1))

rv = multinomial(n=trials, p=[1./sides]*sides)
vals = rv.rvs(sides * 1000) * np.matrix(die).T
prob = (vals == query).sum() / 1. / len(vals)

print 'Environ %d%% de chances d\'obtenir %d en %d jet(s) avec %d faces' % \
      (round(prob*100), query, trials, sides)
