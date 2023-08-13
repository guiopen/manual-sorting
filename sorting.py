#lista = [9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9]
for i in range(1, len(lista)):
    j = i - 1
    while True:
        if lista[i] > lista[j]:
           j += 1
           break
        if j <= 0:
            break
        j -= 1
    lista.insert(j, lista[i])
    lista.pop(i + 1)
#print(lista)
