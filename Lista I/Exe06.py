'''
Crie uma lista chamada lista_a = ["A", "B", "C"].
Crie uma lista_b que seja apenas uma referência para a lista_a.
Crie uma lista_c que seja uma cópia independente de lista_a.
Adicione o elemento "D" à lista_b.
Diga, sem executar o código, o que acontecerá com a lista_a e com a lista_c após essa 
inserção e explique o porquê com base no conceito de passagem por referência.

'''
lista_a = ["A", "B", "C"]
lista_b = lista_a
lista_c = lista_a.copy()

print('Lista A:', lista_a)
print('Lista B:', lista_b)
print('Lista C:', lista_c)

lista_b.append('D')

print('Lista A:', lista_a)
print('Lista B:', lista_b)
print('Lista C:', lista_c)