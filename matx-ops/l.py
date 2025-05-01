#!/usr/bin/env python3
import numpy as np

od = np.random.randint(10,31, size=5)
twd = np.random.randint(1,34, size = (4,4))
thd = np.random.randint(6,67,size=(2,5,6))
print("{}".format(twd))
# print("{}\n{}\n{}".format(od.ndim,od.shape,od.size))

print(twd[::-1,::-1])
