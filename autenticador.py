'''
CPF = 168.995.350-09
-------------------------------------------
1 * 10 = 10               # 1 * 11 = 11
6 * 9 = 54                # 6 * 10 = 60
8 * 8 = 64                # 8 * 9 = 72
9 * 7 = 63                # 9 * 8 = 72
9 * 6 = 54                # 9 * 7 = 63
5 * 5 = 25                # 5 * 6 = 30
3 * 4 = 12                # 3 * 5 = 15
5 * 3 = 15                # 5 * 4 = 20
0 * 2 = 0                 # 0 * 3 = 0
                          # 0 * 2 = 0
        297               #     343
11 - (297 % 11) = 11      #   11 - (343 % 11) = 9
11 > 9 = 0                #
Digito 1 = 0              # Digito 2 = 9
'''
'''cpf =  '202085057'
i = 10
i2 = 0
while i >= 2:
    for valor in cpf:
        v2 = int(valor)
        v3 = v2 * i
        i2 += v3

        i -= 1
i3 = 11 - (i2 % 11)
if i3 <= 9:
    i3 = str(i3)
    cpfnv = cpf + i3

else:
    i3 = '0'
    cpfnv = cpf + i3
a = 11
a2 = 0
while a >= 2:
    for valor2 in cpfnv:
        va2 = int(valor2)
        va3 = va2 * a
        a2 += va3
        a-=1
a3 = 11 - (a2 % 11)
if a3 <= 9:
    a3 = str(a3)
    cpfnovo = cpfnv + a3
    print(cpfnovo)
else:
    a3 = '0'
    cpfnovo = cpfnv + a3'''
cpf = input('Digite seu cpf para validar ele: ')
cpfv = cpf[:-2]
i = 10
i2 = 0
if not cpf.isdigit():
    print('DIGITE APENAS NUMERO,SEM LETRAS E SEM CARACTERES')
elif len(cpf) <= 1:
    print('digite o cpf completo')
else:
    while i >= 2:
        for valor in cpfv:
            v2 = int(valor)
            v3 = v2 * i
            i2 += v3

            i -= 1
    i3 = 11 - (i2 % 11)
    if i3 <= 9:
        i3 = str(i3)
        cpfnv = cpfv + i3

    else:
        i3 = '0'
        cpfnv = cpfv + i3
    a = 11
    a2 = 0
    while a >= 2:
        for valor2 in cpfnv:
            va2 = int(valor2)
            va3 = va2 * a
            a2 += va3
            a-=1
    a3 = 11 - (a2 % 11)
    if a3 <= 9:
        a3 = str(a3)
        cpfnovo1 = cpfnv + a3

    else:
        a3 = '0'
        cpfnovo1 = cpfnv + a3



    if cpfnovo1 == cpf:
        print('Seu cpf e valido, Parabens')
    else:
        print('Este cpf NÃO e valido')
