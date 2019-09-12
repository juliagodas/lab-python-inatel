altura = float(input('Entre com a altura de sua parede (metros): '))
largura = float(input('Entre com a largura de sua parede (metros):'))

area = altura * largura
litro = area/2

print('Sua área é de {} m² e você ira precisar de {} litros de tinta'.format(area,litro))
