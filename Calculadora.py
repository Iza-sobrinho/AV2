operacao = input('''
Por favor escolha a operação que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if operacao == '+':
    print('{} + {} = '.f(n1, n2))
    print(n1 + n2)

elif operacao == '-':
    print('{} - {} = '.f(n1, n2))
    print(n1 - n2)

elif operacao == '*':
    print('{} * {} = '.f(n1, n2))
    print(n1 * n2)

elif operacao == '/':
    print('{} / {} = '.f(n1, n2))
    print(n1 / n2)

else:
    print('Esta não é uma operação viável para este programa.')