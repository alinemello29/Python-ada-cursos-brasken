numero_sorteado = 15

numero_escolhido = (int('infrome uma numero entre  1 e 20'))

if numero_sorteado == numero_escolhido:
    print('voce acertou')
    print('parabéns')

else:
    print('você errou')
    print('tente novamente')

while numero_escolhido != numero_sorteado:
    print('você errou o numero, tente novamente')

numero_escolhido = int(input('informe uma numero entre1 1 e 20'))

print('parabéns! você acertou')
