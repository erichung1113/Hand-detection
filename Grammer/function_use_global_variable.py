cnt=0

def add():
    global cnt 
    #use global variable
    #this name shoule equal to defined global variable
    #It means this cnt is GLOBAL's cnt,not new creation
    #you can image that "global" is a connection to outside-defined variable
    cnt+=1

add()
print(cnt) #1
