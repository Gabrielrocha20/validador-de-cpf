'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend
min, max
range
'''
'''bool = True
int = 10
flut = -10.10
strings = 'textos'
'''
'''
#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#        -5   -4   -3   -2   -1
string = 'ABCDE'
#print(string[1]) vai aparecer o indice 1 que e b
'''
'''
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.insert(2,'b')
#l2.append('b') adiciona
#l2.inset('b') adiciona
#l2.pop() ele tira um indice
#del(l2[0:2]) deleta o valor referente ao indice dele
print(l1)
print(l2)
'''
'''
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
for valor in l1:
    soma = soma + valor
print(soma)'''
'''
l1 = ['string', True, 10, -20.5]
for elem in l1:
    print(f'o tipo de elem e {type(elem)} e seu valor e {elem}')'''
secreto = 'perfume'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('ahhhhhhhh isso nao vale, digite apenas uma letra')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print('Uhuuuuuuuul, a letra {} existe na palavra secreta'.format(letra))
    else:
        print('Affffffffffz, a letra {} NÃO EXISTE  na palavra secreta'.format(letra))
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print('Que legal , VOCÊ GANHOU !!! A palavra era {}'.format(secreto_temporario))
        break
    else:
        print(f'A palavra secreta esta assim : {secreto_temporario}')
    if letra not in secreto:
        chances -= 1
    print('Voce ainda tem {} chances.'.format(chances))
    print()
