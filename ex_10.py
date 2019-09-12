
dist= float(input ('Entre com a distancia: '))

if dist <= 200:
    preco= 0.5 * dist
    print('O preço da passagem é: ', preco)
else:
    preco =  0.45 * dist
    print('O preço da passagem é: ', preco)
