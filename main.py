def imprimir_oi(nome):
    print(f'Hello {nome}')


def somar(numero_a, numero_b):
    return numero_a + numero_b


def subtrair(numero_a, numero_b):
    return numero_a - numero_b


def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'Nao dividiras por zero'


if __name__ == '__main__':
    imprimir_oi('World')

    resultado = somar(7, -6)
    print(f'O resultado é: {resultado}')

    resultado = subtrair(25, 8)
    print(f'A subtração: {resultado}')

    resultado = dividir(27, 3)
    print(f'O divisão é: {resultado}')

    resultado = multiplicar(30, 2)
    print(f'O multiplicação é: {resultado}')
