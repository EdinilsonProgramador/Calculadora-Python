def calculadora():
    operacao = input('Selecione uma operação: + - * /')
    if operacao == '+':
        print('Operação SOMA')
    elif operacao == '-':
        print('Operação SUBTRAÇÃO')
    elif operacao == '*':
        print('Operação MULTIPLICAÇÃO')
    elif operacao == '/':
        print('Operação DIVISÃO')

    numero_1 = int(input("Primeiro Numero:  "))
    numero_2 = int(input("Segundo Numero: " ))
     #adição
    if operacao == '+':
        print('{} + {} = {} ' .format(numero_1, numero_2, numero_1 + numero_2))
    #subtração
    elif operacao == '-':
        print('{} - {} = {}' .format(numero_1, numero_2, numero_1 - numero_2))
    #multiplicação
    elif operacao == '*':
        print('{} x {} = {}' .format(numero_1, numero_2, numero_1 * numero_2))
    #divisão
    elif operacao == '/':
        print('{} / {} = {}' .format(numero_1, numero_2, numero_1 / numero_2))
    else:
        print('Selecione um operador valido por favor')
calculadora()

def again():
    calc_again = input('Gostaria de Realizar outra operação? S para sim, N para não.')

    if calc_again.upper() == 'S':
        calculadora()
    elif calc_again.upper() == 'N':
        print('OBRIGADO')
    else:
        again()
again()
calculadora()

