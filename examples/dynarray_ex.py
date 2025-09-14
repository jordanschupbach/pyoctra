import random

import numpy as np

import pyoctra
from pyoctra import octra

x = np.random.rand(100)

dir(octra)

dir(pyoctra)

pyoctra.__name__

octra.__name__

x = octra.DynArrayDouble(100)
x[0] = 3.14
x[2] = 3.14
x.push_back(4.20)
x.push_back(6.90)
x.size()
dir(x)
x.__class__
y = octra.DynArrayDouble(100)
# x + y


# Don't
for i in range(x.size()):
    x[i] = random.random()

# Do
# octra.fill_runif(x, 0.0, 1.0)

for i in range(x.size()):
    print(x[i])

