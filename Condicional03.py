# LEIA UM NÚMERO E INFORME SE ELE É PAR OU IMPAR
numero = int(input('informe numero: '))

if numero % 2 == 0:
    print(f'o número digitado foi: {numero}, esse número é par')
else:
    print(f'o número digitado foi: {numero}, esse número é impar')