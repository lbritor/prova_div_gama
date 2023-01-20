"""
Elabore um programa que leia um número que o usuário digitar. Dependendo do número informado,
das frases abaixo, o sistema imprimirá somente as que forem verdadeiras.
○ O número é menor que 10.
○ O número é par.
○ O número está entre 8 e 16.
○ O número é 51 ou 80.
"""

numero_escolhido = int(input('Informe um número inteiro: '))

if numero_escolhido < 10:
    print(f'O número {numero_escolhido} é menor que 10.')
if numero_escolhido % 2 == 0:
    print(f'O número {numero_escolhido} é par.')
if 16 >= numero_escolhido >= 8:
    print(f'O número {numero_escolhido} está entre 8 e 16.')
if numero_escolhido == 51 or numero_escolhido == 80:
    print(f'O número digitado é 51 ou 80.')
