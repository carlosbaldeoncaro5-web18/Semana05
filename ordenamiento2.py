def ordernar_seleccion (lista): 
    n = len(lista) 
    for j in range (n-1): 
        imin = j 
        for i in range (j + 1, n): 
            if lista[i] < lista[imin]: 
                imin = i 
        if imin != j: 
            lista[j], lista[imin] = lista[imin], lista[j] 


mi_lista = [2, 8, 5, 3, 9, 4, 1] 
print("Sin ordenar:", mi_lista) 
ordernar_seleccion(mi_lista) 
print("Ordenada:", mi_lista)