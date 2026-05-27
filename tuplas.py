#Tuplas
    # Imutável: Não pode ser modificada após a criação.
    # Ordenada: Mantém a ordem dos elementos.
    # Permite Duplicatas.

frutas = ('Maçã', 'Melão', 'Uva', 'Kiwi', 'Mexerica', 'Tomate')

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
print(frutas[4])
print(frutas[5])

#frutas[1] = 'Melancia' #ERRO

lista_frutas = list(frutas)

lista_frutas[1] = 'Melancia'
print(lista_frutas)


valor_x = ('ana') #STRING
valor_y = ('ana', ) #TUPLA

print(type(valor_x))  #STR
print(type(valor_y))  #TUPLA

#FUNÇÕES COM TUPLAS

# count() --> retorna o numero de vezes de um determinado valor dentro da tupla
# index() --> retorna a psição de um elemento na tupla

tupla_numeros = (1,2,3,4,5,6,7,8,9,0,1,2,3,4,4,5,6)
print('Tupla numeros:', tupla_numeros)
print('Quantas vezes aparece o valor 3:', tupla_numeros.count(4))
print('Em qual posição está o valor 7:', tupla_numeros.index(7))
print('Cinco primeiros elementos da tupla:', tupla_numeros[0:5])
print('Ultimo elemento da tupla:', tupla_numeros[-1])

