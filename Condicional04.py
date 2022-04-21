# LEIA UMA ALTURA E SE A ALTURA FOR INFERIOR A 1.50
# INFORME QUE ELE NÃO PODERÁ ENTRAR NO BRINQUED

altura = float(input('informe a altura da criança:'))

if altura < 1.50:
    print('você nao tem altura suficiente para o brinquedo.')
else:
    print('sua altura está dondizente para o brinquedo.')