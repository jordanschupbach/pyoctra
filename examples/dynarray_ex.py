# from pyoctra.octra import DynArray
from pyoctra import octra

x = octra.DynArrayDouble(100)
x.push_back(4.20)
x.push_back(6.90)
x.size()
print(x)
