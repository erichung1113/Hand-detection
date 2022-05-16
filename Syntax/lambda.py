#lambda is used for defining a funcition

Max=lambda a,b:a if a>b else b
'''
=
def Max(a,b):
  if a>b: return a
  else: return b
'''
Add=lambda a,b:a+b
'''
=
def Add(a,b):
  return a+b
'''
print(Add(4,6)) #10 
print(Max(3,6)) #6
