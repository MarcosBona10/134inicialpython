import json
import os
import requests

url = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type': 'application/json'}

def teste_vender_pet():
    # Dados de entrada
    # Virão do arquivo pedido1.json

    # Resultados esperados
    status_code_esperado = 200
    pedido_id_esperado = 582645987
    pet_id_esperado = 2754371
    status_pedido_esperado = 'placed'

    # Executa
    caminho = os.path.abspath(__file__ + "/../../../") + os.sep + 'vendors' + os.sep + 'json' + os.sep


    resultado_obtido = requests.post(

        url=url + 'store/order',
        headers=headers,
        data=open(caminho + 'pedido1.json')

    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pedido_id_esperado
    assert corpo_do_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado

    # Extrai

    pet_id_extraido = corpo_do_resultado_obtido.get('petId')

    # Configura
    # Dados de entrada
    # Extraido da 1 transação acima

    # Resultado esperado
    pet_name_esperado = 'Kratos'
    status_code_esperado = 200

    # Executa
    resultado_obtido = requests.get(
        url=url + 'pet/' + str(pet_id_extraido),
        headers=headers
    )

    # Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))
    assert corpo_do_resultado_obtido['name'] == pet_name_esperado

