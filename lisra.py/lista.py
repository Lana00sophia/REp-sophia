lista = []
print(type(lista))
#Lista pronta
frutas = ["romã","banana","abacaxi","laranja"]
#add elementos e o "local" ,ou seja, a posição do index
frutas.insert(1,"manga")
print(frutas)

#outro jeito de add elementos: soma de listas 
frutas_favoritas = ["melancia","jabuticaba","romã"]
frutas+=frutas_favoritas
print(frutas)
 
#remover elementos
print("Removendo elementos")
frutas.remove("romã")
print(frutas)
print("contando elementos(mostra sua localização)")
print(frutas.count("romã"))
#nome da lista,bota o ponto o pop deleta,entre os parenteses a posição do elemento
print("tirando uma fruta")
frutas.pop(3)
print(frutas)

print("escolhendo elementos específicos fora de ordem")
frutas2 = frutas[2:4]
print(frutas2)
 
#copiar listas
frutas2 = frutas[:]
frutas2 = frutas.copy()
print("copiando listas")
print(frutas2)
print(id(frutas))
print(id(frutas2))
#add vários elementos de uma vez
frutas.extend("mamão")

#mudando a sequência
frutas.sort()
frutas.reverse()
print(frutas)
