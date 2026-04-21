num_cubitos = [2,8,5,3,9,4] 
for i in range(1, len(num_cubitos)): 
    num_cb = num_cubitos[i] 
    j= i - 1 
    while j >= 0 and num_cb < num_cubitos[j]: 
        num_cubitos [j + 1] = num_cubitos[j] 
        j = j-1 
        num_cubitos[j +1] = num_cb 
print(num_cubitos)