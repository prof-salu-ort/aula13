'''
Você recebeu a seguinte lista desordenada de notas de alunos: 
notas = [7.5, 9.0, 5.2, 8.0, 6.5].
Use uma função que ordene a lista de forma crescente, mas que não modifique a 
lista original (salve o resultado em uma nova variável).
Verifique se a nota 5.2 está presente na lista original usando o operador in.
Descubra e exiba a posição (índice) da nota 9.0 na lista original.
'''

notas = [7.5, 9.0, 5.2, 8.0, 6.5]
notas_ordenadas = sorted(notas)

print('Notas:', notas)
print('Notas ordenadas:', notas_ordenadas)
existe = 'SIM' if 5.2 in notas else 'NÃO'
print('Existe a nota 5.2:', existe)
print('Existe a nota 5.2:', 5.2 in notas)
print('A nota 9.0 esta na posicao', notas.index(9.0))
