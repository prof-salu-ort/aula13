'''
Crie uma lista de compras contendo ["arroz", "feijão", "carne", "legumes", "alface"].
- Remova o item "carne" utilizando o método remove().
- Utilize o método pop() para remover e salvar em uma variável o último item da lista ("alface").
- Exiba a lista modificada e o item que foi removido pelo pop().
'''

compras = ["arroz", "feijão", "carne", "legumes", "alface"]

compras.remove("carne") #remove a primeira aparição do elemento
item_removido = compras.pop() #remove e retorna o ultimo elemento da lista

print('Lista atual:', compras)
print('Item removido:', item_removido)