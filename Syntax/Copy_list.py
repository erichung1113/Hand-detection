import copy

#1 D

a=[0]*5
#Method 1
b=a*1
#Method 2
b=a[:] 
#Method 3
b=copy.copy(a)


#2 D

a=[[0]*5]*5
#Method 1
b=copy.deepcopy(a)
