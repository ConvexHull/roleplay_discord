from scipy.stats import multinomial
import json
import numpy as np
import sys

np.random.seed(0)

query = int(sys.argv[1]) if len(sys.argv) > 1 else 3
trials = int(sys.argv[2]) if len(sys.argv) > 2 else 1
sides = json.loads(sys.argv[3]) if len(sys.argv) > 3 else 6
die = sides if isinstance(sides, list) else range(1, sides+1)

# TODO There is a closed form we can use in most cases
# http://mathworld.wolfram.com/Dice.html
rv = multinomial(n=trials, p=[1./len(die)]*len(die))
vals = rv.rvs(max(len(die) * 1000, 10000)) * np.matrix(die).T
prob = (vals == query).sum() / 1. / len(vals)

print 'Roughly %d%% chances of rolling a %d with %d dice of %d faces each' % \
      (round(prob*100), query, trials, len(die))
