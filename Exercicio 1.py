while True:
#Área de entrada dos dados sobre o nome e a idade de determinado aluno(@)
    nome= str(input('Nome:'))
    idade= int(input('Idade:'))

#Código de identificação de ensino de acordo com a faixa etária de determinado aluno(@)
    if 1<= idade <= 5:
        print(f'O aluno(a) {nome} tem {idade} anos e está na educação infantil')
    elif 6<= idade <= 10:
        print(f'O aluno(a) {nome} tem {idade} anos e está no ensino fundamental 1')
    elif 11<= idade <=14:
        print(f'O aluno(a) {nome} tem {idade} anos e está no ensino fundamental 2')
    elif idade >=15:
        print(f'O aluno(a) {nome} tem {idade} anos e está no ensino médio')

#Opção caso o usuário deseja continuar ou não com o programa
        resposta=str(input('Deseja continuar? 0-Não 1-Sim'))
        if resposta=="0":
            break

