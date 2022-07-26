from importlib import import_module
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
from prints import print_input


def get_pokemon_name():
    '''
    função get_pokemon_name 
    busca a lista de pokémons através de uma requisição em um arquivo txt do GitHub,
    Retorna uma lista com o nome de todos os pokémon.
    '''
    all_gem = []
    response = requests.get('https://github.com/cervoise/pentest-scripts/blob/master/password-cracking/wordlists/pokemon-list-en.txt')
    soup = BeautifulSoup(response.text, 'html.parser')
    all_poke_name = soup.find_all('td', {'class': 'blob-code blob-code-inner js-file-line'})
    for pokemon_name in all_poke_name:
        all_gem.append(pokemon_name.text)
    return all_gem


def get_input():
    input_teste = print_input()
    recebe = input_teste.print_input()
    return recebe


def get_data_api(list_pokemon, type):
    '''
    Função get_data_api: 
    iremos receber o valor das duas funções anteriores -> ( Lista de pokemons , Tipo de Pokémon)
    retorna uma lista com o nome dos pokémon que tem o tipo escolhido em primeira posição na pokedex
    '''
    pokemon_list = []
    for pokemon in tqdm (list_pokemon, desc="Loading…", ascii=False, ncols=100):
        headers = {
            'Accept': 'application/json',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Origin': 'https://graphqlpokemon.favware.tech',
        }
        json_data = {
            'query': '{\n\tgetPokemon(pokemon: '+ pokemon + ' reverseFlavorTexts: true takeFlavorTexts: 1) {\n\t\tnum\n\t\tspecies\n\t\ttypes\n\t\tabilities { first second hidden }\n\t\tbaseStats { hp attack defense specialattack specialdefense speed }\n\t\tgender { male female }\n\t\theight\n\t\tweight\n\t\tflavorTexts { game flavor }\n\t\tevYields { hp attack defense specialattack specialdefense speed }\n\t\tisEggObtainable\n\t\tminimumHatchTime\n\t\tmaximumHatchTime\n\t\tlevellingRate\n\t\tsprite\n\t\tshinySprite\n\t\tbackSprite\n\t\tshinyBackSprite\n\t\tsmogonTier\n\t\tsmogonPage\n\t\tserebiiPage\n\t\tbulbapediaPage\n\t}\n}',
        }

        response = requests.post('https://graphqlpokemon.favware.tech/', headers=headers, json=json_data)
        json_response = response.json()
        try:
            if type in json_response['data']['getPokemon']['types'][0]:
                    my_poke_dict = {
                        'Pokémon': pokemon,
                        'HP': json_response['data']['getPokemon']['baseStats']['hp'],
                        'Ataque': json_response['data']['getPokemon']['baseStats']['attack'],
                        'Defesa': json_response['data']['getPokemon']['baseStats']['defense'],
                        'SP Attack': json_response['data']['getPokemon']['baseStats']['specialattack'],
                        'SP Defense': json_response['data']['getPokemon']['baseStats']['specialdefense'],
                        'Info Bulbapédia':json_response['data']['getPokemon']['bulbapediaPage']
                    }
                    pokemon_list.append(my_poke_dict)
        except KeyError:
            pass
    return pokemon_list

def get_response():
    headers = {
        # 'Accept-Encoding': 'gzip, deflate, br',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://graphqlpokemon.favware.tech',
    }
    json_data = {
        'query': '{\n\tgetPokemon(pokemon: '+ 'charmander' + ' reverseFlavorTexts: true takeFlavorTexts: 1) {\n\t\tnum\n\t\tspecies\n\t\ttypes\n\t\tabilities { first second hidden }\n\t\tbaseStats { hp attack defense specialattack specialdefense speed }\n\t\tgender { male female }\n\t\theight\n\t\tweight\n\t\tflavorTexts { game flavor }\n\t\tevYields { hp attack defense specialattack specialdefense speed }\n\t\tisEggObtainable\n\t\tminimumHatchTime\n\t\tmaximumHatchTime\n\t\tlevellingRate\n\t\tsprite\n\t\tshinySprite\n\t\tbackSprite\n\t\tshinyBackSprite\n\t\tsmogonTier\n\t\tsmogonPage\n\t\tserebiiPage\n\t\tbulbapediaPage\n\t}\n}',
    }
    response = requests.post('https://graphqlpokemon.favware.tech/', headers=headers, json=json_data)
    return response.status_code

def load_csv(api, type):
    '''
    Função save_csv
    recebe o parâmetro api ( lista de nomes dos pokémons de determinado tipo )
    e retorna um csv com o nome de todos os pokémons daquele tipo selecionado 
    (Lembrando que o pokémon tem que constar na lista de requisição)
    '''
    with open(f'pokemons_{type}_list.csv', 'w', encoding='utf8', newline='') as csv_file:
        fieldnames = list(api[0].keys())
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dict_key in api:
            writer.writerow(dict_key)


def main():
    poke_name = get_pokemon_name()
    input = get_input()
    print(f'Então o seu tipo de pokémon favorito é {input}?! Pode deixar!')
    get_api = get_data_api(poke_name, input)
    print(f'Segue uma lista dos pokémon do tipo {input} que encontrei:')
    csv_save = load_csv(get_api, input)

if __name__ == '__main__':
    main()
