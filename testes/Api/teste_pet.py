# bibliotecas
import json
from testes.utils.file_manager import ler_csv
import pytest
import requests

# variaveis publicas
url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


# definições das funções (defs)

def teste_incluir_pet():
    # Configura / Prepara
    # Dados de entrada provem do pet1.json

    # Resultados esperados
    status_code_esperado = 200
    pet_id_esperado = 5416173
    pet_nome_esperado = "Kratos"
    pet_nome_categoria_esperado = "Pitbull"
    pet_nome_tag_esperado = "vacinado"

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\marcos.mota\\PycharmProjects\\134inicial\\vendors\\Json\\Pet1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado


def teste_consultar_pet():
    # Configura
    # Entrada
    pet_id = '5416173'

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 5416173
    pet_nome_esperado = "Kratos"
    pet_nome_categoria_esperado = "Pitbull"
    pet_nome_tag_esperado = "vacinado"

    # Executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado


def teste_alterar_pet():
    # Configura
    # Dados de entrada virão do pet2.json

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 5416173
    pet_nome_esperado = "Kratos"
    pet_nome_categoria_esperado = "Pitbull"
    pet_nome_tag_esperado = "vacinado"
    pet_status_esperado = 'placed'

    # Executa
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('C:\\Users\\marcos.mota\\PycharmProjects\\134inicial\\vendors\\Json\\Pet2.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado
    assert corpo_do_resultado_obtido['status'] == pet_status_esperado


def teste_excluir_pet():
    # Configura
    # Dados de entrada virão do pet2.json
    pet_id = '5416173'

    # Resultados Esperados
    status_code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = '5416173'

    # Executa
    resultado_obtido = requests.delete(
        url=url + '/' + pet_id,
        headers=headers,
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == status_code_esperado
    assert corpo_do_resultado_obtido['type'] == type_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada


@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags_id,tags_name,status', ler_csv(
    'C:\\Users\\marcos.mota\\PycharmProjects\\134inicial\\vendors\\csv\\massa_incluir_pet.csv'))
def teste_incluir_pet_em_massa(pet_id, category_id, category_name, pet_name, tags_id, tags_name, status):
    # Configura
    # Dados de entrada
    # Os dados de entrada  proveem do arquivo massa_incluir_pet_.csv
    # Montagem do JSON dinâmico

    corpo_json = '{'
    corpo_json += f'  "id": {pet_id},'
    corpo_json += '       "category": {'
    corpo_json += f'            "id": {category_id},'
    corpo_json += f'            "name": "{category_name}"'
    corpo_json += '        },'
    corpo_json += f'        "name": "{pet_name}",'
    corpo_json += '        "photoUrls": ['
    corpo_json += '            "string"'
    corpo_json += '        ],'
    corpo_json += '        "tags": ['
    corpo_json += '            {'
    corpo_json += f'                "id": {tags_id},'
    corpo_json += f'                "name": "{tags_name}"'
    corpo_json += '            }'
    corpo_json += '        ],'
    corpo_json += f'        "status": "{status}"'
    corpo_json += '}'

    # Resultado esperado
    # Os dados de entrada também servirão como resultados
    # esperados, visto que o retorno é um eco
    status_code_esperado = 200

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )

    # Valida

    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    assert corpo_do_resultado_obtido['tags'][0]['name'] == tags_name
