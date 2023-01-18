print('Calculadora Feita em Python by: Luiz Valmir (Scorpion :D)')
print('Para encerrar basta digitar : encerrar')
select = ''  # valor aleatorio apenas para que a variavel seja definida
while (select != 'encerrar'):
    select = input('Que operação voce deseja realizar:')

    # função para somar dois numeros
    def soma(n1, n2):
        resultado = n1+n2
        print(resultado)
    # função para subtrair dois numeros

    def subtração(n1, n2):
        resultado = n1-n2
        print(resultado)
    # função para multiplicar dois numeros

    def multiplicação(n1, n2):
        resultado = n1*n2
        print(resultado)
    # função para dividir dois numeros

    def divisão(n1, n2):
        resultado = n1/n2
        print(resultado)
    # condições criadas para o programa chamar a operação que o usuário deseja
    if (select == 'soma'):
        x = int(input('Digite o primeiro numero:'))
        y = int(input('Digite o segundo numero:'))
        soma(x, y)

    if (select == 'subtração'):
        x = int(input('Digite o primeiro numero:'))
        y = int(input('Digite o segundo numero:'))
        subtração(x, y)

    if (select == 'multiplicação'):
        x = int(input('Digite o primeiro numero:'))
        y = int(input('Digite o segundo numero:'))
        multiplicação(x, y)

    if (select == 'divisão'):
        x = int(input('Digite o primeiro numero:'))
        y = int(input('Digite o segundo numero:'))
        divisão(x, y)
    # caso o usuário deseje encerrar o programa
    elif (select == 'encerrar'):
        exit()
