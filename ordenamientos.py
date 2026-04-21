def ordseleccion(lst):
    n= len(lst)
    for manoizq in range (n-1):
        posMen = manoizq
        for ver in range(manoizq+1, n):
            if lst [posMen] > lst[ver]:
                posMen = ver 
        lst [ manoizq], lst[posMen] = lst[posMen], lst[manoizq]
        


list = [2,8,5,3,9,4,1]
ordseleccion(list)
print(list)