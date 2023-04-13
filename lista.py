# > listas

#listas


#antes
nota1: 7.9
nota2: 9.7
nota3: 8.2

#com listas
notas = [7.9, 9.7, 8.2]

#criando lista vazia
lista = []
lista = list()

lista = [26, aline, 3.1405, true]
lista_de_lista =[10,[1,2,3]]

#indexação e slices(fatiamento)

lista = [10, aline, 3.476, false]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#slices
listas = [10,50,30,40,25,60,5]

print(lista[0.3])
print(lista[3.6])
print(lista[3:])
print(lista[2:6:2])

#>iterações com for

#1 utilizando os proprios elementos da listas

for elemento in lista:
    print(elemento)
    
#2 utilizando os indices

    print('comprimento da lista:', len(lista))

for i in range (len(lista)):

    print(lista[i])