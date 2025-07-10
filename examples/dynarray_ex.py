from pyoctra import octra

x = octra.DynArrayDouble(100)
x[0] = 3.14
x[2] = 3.14
x.push_back(4.20)
x.push_back(6.90)
x.size()
dir(x)
x.__class__
y = octra.DynArrayDouble(100)
x + y

