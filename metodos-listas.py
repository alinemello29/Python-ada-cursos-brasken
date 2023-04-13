# > metedos de listas

listas = [1, 3, 12, 8, 2]

#append
print('antes do append:', lista)

lista.append(3)
print('depois do append:', lista)

#insert
lista.insert(2,10)

print('depois do insert:', lista)

#extend
lista = [1,2,3]

lista.extend(lista2)
print('depois do extend:', lista)

#pop
print('lista apos o pop:', lista)

lista.pop(0)
print('lista apos o pop:', lista )

#remove
lista.remove(3)
print('depois do remove:', lista )

#count
print('quantidate de 2 na lista:', lista.count(2))

#index
print('indice do elemento12:', lista. index(12))

#sort
lista.sort()
print(lista)

#funções para listas

#len
print(len(lista))

#sum
print(sum(lista))

#max (maior)
print('maior elemento da lista:', max(lista))

#min(menor)
print('menor elemento da lista:', min(lista))