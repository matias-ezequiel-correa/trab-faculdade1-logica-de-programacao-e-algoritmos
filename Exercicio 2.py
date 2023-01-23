nome= str(input('Digite um nome:')).upper()
print(nome)

for letra in nome:
    if letra=="A":
        print('@', end='')
    elif letra=='E':
        print('&', end='')
    elif letra=='I':
        print('!', end='')
    elif letra=='O':
        print('#', end='')
    elif letra=='U':
        print('*', end='')
    else:
        print(letra, end='')

