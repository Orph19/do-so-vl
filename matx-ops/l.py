#!/usr/bin/env python3
import numpy as np
np.random.seed(0)
# rd = np.random.randn(50)
# ud = np.random.rand(50)

# # print(np.mean(rd),np.min(rd),np.max(rd),np.std(rd))

# # print(np.mean(ud),np.std(ud))
# print(sum(np.where(rd>0.5,True,False)))

# ma = np.zeros((5,5),dtype=float)
# ma[1:4,1:4] = 1
# mb = np.ones((5,5),dtype=float)*5
# wt = ma*1.5
# print(wt.T[:,1:2])

total_time = 10.0
num_steps = 50
t = np.linspace(0,total_time,num_steps)


initial_position = 0.0
constant_velocity = 2.5

positions = np.zeros(num_steps)
positions = initial_position + constant_velocity*t
print(positions)
