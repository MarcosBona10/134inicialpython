import pytest

from main import somar, subtrair, multiplicar, dividir


def teste_somar():
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15
    resultado_obtido = somar(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado


def teste_subtrair():
    numero_a = 15
    numero_b = 10
    resultado_esperado = 5
    resultado_obtido = subtrair(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado


def teste_multiplicar():
    numero_a = 3
    numero_b = 4
    resultado_esperado = 12
    resultado_obtido = multiplicar(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado


def teste_dividir_positivo():
    numero_a = 27
    numero_b = 3
    resultado_esperado = 9
    resultado_obtido = dividir(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado


def teste_dividir_negativo():
    numero_a = 27
    numero_b = 0
    resultado_esperado = 'Não dividirás por zero'
    resultado_obtido = dividir(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado


# Lista para uso com massa de teste
lista_de_valores = [

    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)
]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    # Quando trabalhar com  LISTAS não pode ter numeros fixados
    # 1 - Configura
    # Utilizamos a lista  como massa de teste

    resultado_obtido = somar(numero_a, numero_b)
    assert resultado_obtido == resultado_esperado
