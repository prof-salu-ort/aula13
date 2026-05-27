'''
Dada a string tecnologia = "Python", converta-a em uma lista de caracteres chamada letras_lista. 
Depois, faça as seguintes alterações:
 - Adicione o caractere "3" ao final da lista utilizando o método apropriado.
 - Insira o caractere "!" no início da lista (índice 0).
 - Exiba o resultado final e o tamanho total da lista usando len().

'''
tecnologia = 'Python'
letras_lista = list(tecnologia)

print('Tamanho:', len(letras_lista)) #lenght

letras_lista.append('3') #adiciona eno final da lista
letras_lista.insert(0, '!') #adiciona na posição informada

print('Tamanho:', len(letras_lista)) #lenght
print(letras_lista)

