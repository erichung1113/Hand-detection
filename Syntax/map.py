#map is a function to change all elements to other style
#map([changed_type_or_function],[variable])
#map's return value is a "map object",please use list to change into type which you can understand.

a=['1','2','3'] #str
a=list(map(int,a)) # ->int
print(a[0]+1) #2


def mul(x):
    return x*2

b=[1,2,3]
b=list(map(mul,b)) 
print(b) #[2, 4, 6]
