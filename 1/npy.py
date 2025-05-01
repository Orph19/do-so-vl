#!/usr/bin/env python3
import numpy as np
from py import Matrix

m1 = np.linspace(4,114,12, dtype=int).reshape(3,4)
m2 = np.linspace(6,93,12, dtype=int).reshape(4,3)

d1 = Matrix(m1.tolist(), (3,4))

d2= Matrix(m2.tolist(), (4,3))

result1 = m1 @ m2
check_result1 = d1.mul(d2)

print(result1,check_result1, sep="\n")  






