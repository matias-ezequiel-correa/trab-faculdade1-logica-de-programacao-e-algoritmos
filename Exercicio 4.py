from random import randint

inscritos= []

while True:
    print('-------------MENU-------------')
    print('''
1 - Nova inscrição
2 - Visualizar inscrição
0 - Encerrar''')
    escolha = int(input('Opção escolhida:'))
    if escolha == 1:
        novo_dicionario = {'voucher': int(), "nome": str(), 'email': str(), 'telefone': int(), 'curso': str()}
        novo_dicionario['voucher'] = randint(100, 400)
        novo_dicionario['nome'] = str(input('Digite seu nome: '))
        novo_dicionario['email'] = str(input('Digite email: '))
        novo_dicionario['telefone'] = int(input('Digite telefone: '))
        novo_dicionario['curso'] = str(input('Digite curso: '))
        inscritos.append(novo_dicionario)

    elif escolha == 2:
        print('-------------Lista inscritos-------------')
        if len(inscritos) == 0:
            print('Nenhuma inscrição cadastrada')
        else:
            for dic in inscritos:
                for k, v in dic.items():
                    print(f'{k} : {v}')
                print()


    elif escolha == 0:
        break
    else:
        print('Erro: digite uma opção válida!')




