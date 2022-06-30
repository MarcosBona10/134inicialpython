# Done: 1 - criar um teste que adicone um usuário
# Done: 2 - realizar o login e extrair o token da resposta
# Done: 3 - criar uma venda de um pet para um usuário
# Done: 4 - consultar os dados do pet que foi vendido
import json

import requests

url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}
token = ''


def teste_incluir_user():
    # Dados de entrada
    # Virao do arquivo user1.json

    # Resultado esperado
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = '2754371'

    # Executa
    resultado_obtido = requests.post(

        url=url,
        headers=headers,
        data=open('C:\\Users\\marcos.mota\\PycharmProjects\\134inicial\\vendors\\Json\\user1.json')

    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == code_esperado
    assert corpo_do_resultado_obtido['type'] == type_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada


def teste_login():
    # Dados de entrada
    username = 'Carlos'
    password = 'Happy'

    # Resultado esperado
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = 'logged in user session:'

    # Executa
    resultado_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers,
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == code_esperado
    assert corpo_do_resultado_obtido['type'] == type_esperado
    assert mensagem_esperada.find(corpo_do_resultado_obtido['message'])

    # Extrai

    mensagem_extraida = corpo_do_resultado_obtido.get('message')
    print(f'O token = {mensagem_extraida}')
    token = mensagem_extraida[23:]
    print(f'O token = {token}')

    # [inicio : fim : passos]
