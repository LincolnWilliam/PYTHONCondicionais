# VERIFIQUE UMA SENHA FORNECIDA PELO USUARIO
# SE ELA FOR IGUAL A 12345 INFORME QUE O ACESSO É
# PERMITIDO, SENÃO INFORME QUE O ACESSO ESTÁ NEGADO

senha = int(input('digite sua senha: '))

if senha == 12345:
    print('acesso permitido!')
else:
    print('acesso negado!')
