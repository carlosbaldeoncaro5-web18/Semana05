cubo = [2,8,5,3,9,4,1] 
for i in range (len(cubo)): 
    for j in range(0, len(cubo) -i -1): 
        if cubo[j] > cubo[j + 1]: 
            cb = cubo[j] 
            cubo[j] = cubo[j+1] 
            cubo[j+1] = cb 

print (cubo)