import copy

#1 D
a=[0]*5
#Method 1
b=a[:] 
#Method 2
b=copy.copy(a)

#2 D
a=[[0]*5]*5
#Method 1
b=copy.deepcopy(a)
