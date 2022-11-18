medida = float (input('A medida em Litros: '))
kl = medida / 1000
hl = medida / 100
dal = medida / 10
dl = medida * 10
cl = medida * 100
ml = medida * 1000
print('A medida de {:.0f}l corresponde: {}kl {}hl {}dal {:.0f}dl {:.0f}cl e {:.0f}ml'.format(medida, kl, hl, dal, dl, cl, ml))