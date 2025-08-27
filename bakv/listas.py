#Diferencia de listas

lista_vacia = []

lista_numeros = [1, 2, 3, 4, 5]

lista_string = ["manzana", "pera", "uva"]

lista_mixta = ["hola", 1, True]

#Métodos básicos python
#append = agrega al final
lista_string.append("sandía")
print(lista_string)

#insert= necesita un índice así: (1, "algo")
lista_string.insert(1, "guinda")
print(lista_string)

#quitar o remover elemento
lista_string.remove("pera")
print(lista_string)

#metodos de busqueda
numeros = [10, 20, 30 , 40, 50, 30, 20]
indice = numeros.index(30)
print("El índice de 30 ", indice)

#para saber el total de elementos de una lista

total = len(numeros)
print(total)

#mmetodo de ordenamiento

numeros_azar = [2 ,4, 7, 23, 45, 6235, 76894, 12, 23, 11]

numeros_azar.sort()
print("Lista ordenada ascendente", numeros_azar )

numeros_azar.sort(reverse=True)

#Combinas listas

frutas = ["manzana", "uva", "pera"]
verduras = ["apio", "cebolla", "lechuga"]

print("Fruta-Verdura")
for i in range(len(frutas)):
    print(f"{frutas[i]} - {verduras[i]}")
    
    
#Comparar elementos
lista1 = [5,8,3,9,2]
lista2 = [5,7,3,10,2]

for i in range(len(lista1)):
    if lista1[i] == lista2[i]:
        print(f"indice {i}: {lista1[i]} == {lista2[i]} ")
        
        
