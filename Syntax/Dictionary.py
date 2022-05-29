heights={"Mike":170,"Peter":165}

print(heights.keys()) #->dict_keys(['Mike', 'Peter'])
print(heights.values()) #->dict_values([170, 165])

for key,value in heights.items():  #print all keys and values
    print(key,value)  

del heights["Mike"] #delet elements

heights.get("Peter",-1) #return "Peter"'s value, the second variable is a return value when "Peter" is not in the map

