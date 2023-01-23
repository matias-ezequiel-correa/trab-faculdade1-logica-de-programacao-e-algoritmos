#Código para a apresentação do hotel e as especificações das posições de cada quarto
print('-----HOTEL DE ANIMAIS-----')
print('Especificando posições:')
a = [1,2,3,4]
b = [5,6,7,8]

print(a)
print(b)
print('')

#Começo e explicação da primeira fase do jogo e as especificações de cada quarto segundo seu estado, caso esteja indisponíveis ou ocupada por um hóspede.
print('Bem-vindo a Fase 1!')
print('Na Fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos:')

a[0] = '*'
a[1] = '*'
a[2] = '_'
a[3] = 'G'
b[0] = 'R'
b[1] = '_'
b[2] = '*'
b[3] = '*'
print(a)
print(b)

while True:
#Entrada: código para as perguntas da Fase 1
    b = int(input('-Em qual posição quer alocar o RATO?'))
    a = int(input('-E em qual posição quer alocar o GATO?'))

#Saída: código segundo a resposta digitada pelo jogador, caso ele acerte, avançará de fase, mas caso as respostas sejam incorreta, ele perderá e o jogo acabará nesse instante
    if b == 6 and a == 3:
        print('Você acertou!! Avançou para a seguinte fase!')
    elif b!= 6 or a!= 3:
        print('Você perdeu!')
        break
    elif b != a:
        print("Você perdeu!")
        break

#Código caso o jogador avance de fase que aparecerá novamente a apresentação do hotel e as especificações das posições de cada quarto
    print('')
    print("-----HOTEL DE ANIMAIS-----")

    print('Especificando posições:')
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    print(a)
    print(b)
    print('')

#Começo e explicação da segunda fase do jogo e as especificações de cada quarto segundo seu estado, caso esteja indisponíveis ou ocupada por um hóspede.
    print('Bem-vindo a Fase 2!')
    print('Na Fase 2, o jogador deve alocar o CÃO,CÃO e OSSO na seguinte matriz que representa os quartos:')
    a[0] = '_'
    a[1] = '*'
    a[2] = '*'
    a[3] = '*'
    b[0] = '*'
    b[1] = 'C'
    b[2] = '_'
    b[3] = '_'
    print(a)
    print(b)

#Entrada: código para as perguntas da Fase 2
    pergunta1 = int(input('-Em qual posição quer alocar o primeiro CÃO?'))
    pergunta2 = int(input('-Em qual posição quer alocar o segundo CÃO?'))
    pergunta3 = int(input("-Em qual posição quer alocar o OSSO?"))

#Saída: código segundo a resposta digitada pelo jogador, caso ele acerte, avançará de fase, mas caso as respostas sejam incorreta, ele perderá e o jogo acabará nesse instante
    if pergunta1 == 7 or 8:
        print("Você acertou!! Avançou para a seguinte fase!")
    elif pergunta1 != 7 or 8:
        print("Você perdeu!")
        break
    elif pergunta2 == 7 or 8:
        print("Você acertou!! Avançou para a seguinte fase!")
    elif pergunta2 != 7 or 8:
        print("Você perdeu!")
        break
    elif pergunta3 == 1:
        print("Você acertou!! Avançou para a seguinte fase!")
    elif pergunta3 != 1:
        print("Você perdeu!")
        break

#Código caso o jogador avance de fase que aparecerá novamente a apresentação do hotel e as especificações das posições de cada quarto
    print('')
    print("-----HOTEL DE ANIMAIS-----")

    print('Especificando posições:')
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    print(a)
    print(b)
    print('')

#Começo e explicação da terceira fase do jogo e as especificações de cada quarto segundo seu estado, caso esteja indisponíveis ou ocupada por um hóspede.
    print('Bem-vindo a Fase 3!')
    print('Na fase 3 o jogador deverá alocar o GATO, RATO e OSSO na seguinte matriz que representa os quartos:')
    a[0] = '_'
    a[1] = '*'
    a[2] = '*'
    a[3] = '*'
    b[0] = '_'
    b[1] = 'G'
    b[2] = '_'
    b[3] = '*'
    print(a)
    print(b)

#Entrada: código para as perguntas da Fase 3
    pergunta4 = int(input('-Em qual posição quer alocar o GATO?'))
    pergunta5 = int(input('-Em qual posição quer alocar o RATO?'))
    pergunta6 = int(input("-Em qual posição quer alocar o OSSO?"))

#Saída: código segundo a resposta digitada pelo jogador, caso ele acerte, avançará de fase, mas caso as respostas sejam incorreta, ele perderá e o jogo acabará nesse instante
    if pergunta4 == 7 :
        print("Você acertou!! Avançou para a seguinte fase!")
    elif pergunta4 != 7 :
        print("Você perdeu!")
        break
    elif pergunta5 == 1 :
        print("Você acertou!! Avançou para a seguinte fase!")
    elif pergunta5 != 1 :
        print("Você perdeu!")
        break
    elif pergunta6 == 5:
        print("Você acertou!! Avançou para a seguinte fase!")
    elif pergunta6 != 5:
        print("Você perdeu!")
        break

#Código caso o jogador avance de fase que aparecerá novamente a apresentação do hotel e as especificações das posições de cada quarto
    print('')
    print("-----HOTEL DE ANIMAIS-----")

    print('Especificando posições:')
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    print(a)
    print(b)
    print('')

#Começo e explicação da quarta e última fase do jogo e as especificações de cada quarto segundo seu estado, caso esteja indisponíveis ou ocupada por um hóspede.
    print('Bem-vindo a Fase 4!')
    print('Na fase 4, o jogador deverá alocar o QUEIJO, QUEIJO e OSSO na seguinte matriz que representa os quartos:')
    a[0] = '_'
    a[1] = '_'
    a[2] = '_'
    a[3] = '*'
    b[0] = '*'
    b[1] = 'R'
    b[2] = '*'
    b[3] = '*'
    print(a)
    print(b)

#Entrada: código para as perguntas da Fase 4
    pergunta7 = int(input('-Em qual posição quer alocar o primeiro QUEIJO?'))
    pergunta8 = int(input('-Em qual posição quer alocar o segundo QUEIJO?'))
    pergunta9 = int(input("-Em qual posição quer alocar o OSSO?"))

#Saída: código segundo a resposta digitada pelo jogador, caso ele acerte, ganhará o jogo, mas caso as respostas sejam incorreta, ele perderá e o jogo acabará nesse instante
    if pergunta7 == 1 or 3:
        print("Você ganhou!! Parabéns jogador!")
        break
    elif pergunta7 != 1 or 3:
        print("Você perdeu!")
        break
    elif pergunta8 == 1 or 3:
        print("Você ganhou!! Parabéns jogador!")
        break
    elif pergunta8 != 1 or 3:
        print("Você perdeu!")
        break
    elif pergunta9 == 2:
        print("Você ganhou!! Parabéns jogador!")
        break
    elif pergunta9 != 2:
        print("Você perdeu!")
        break
