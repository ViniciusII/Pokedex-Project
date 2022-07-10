import requests
from bs4 import BeautifulSoup
import csv

'''
função get_pokemon_name 
busca a lista de pokémons através de uma requisição em um arquivo txt do GitHub,
Retorna uma lista com o nome de todos os pokémon.
'''
def get_pokemon_name():
    all_gem = []
    response = requests.get('https://github.com/cervoise/pentest-scripts/blob/master/password-cracking/wordlists/pokemon-list-en.txt')
    soup = BeautifulSoup(response.text, 'html.parser')
    all_poke_name = soup.find_all('td', {'class': 'blob-code blob-code-inner js-file-line'})
    for pokemon_name in all_poke_name:
        all_gem.append(pokemon_name.text)
    return all_gem


'''
Função get_input 
é uma função de interação com o usuário, 
aonde é perguntado seu tipo de pokémon favorito
retorna o valor escolhido por um usuário.
'''
def get_input():
    usuario_teste = input('''Digite o Número do tipo de Pokémon que você mais gosta!
    ============================================================
    [1] Normal                                                 =
    [2] Fire (Fogo)                                            =
    [3] Water (Água)                                           =
    [4] Grass (Grama)                                          =
    [5] Flying (Voador)                                        =
    [6] Fighting (Lutador)                                     =
    [7] Poison (Veneno)                                        =
    [8] Electric (Elétrico)                                    =
    [9] Ground (Terra)                                         =
    [10] Rock (Pedra)                                          =
    [11] Psychic (Psíquico)                                    =
    [12] Ice (Gelo)                                            =
    [13] Bug (Inseto)                                          =
    [14] Ghost (Fantasma)                                      =
    [15] Steel (Ferro)                                         =
    [16] Dragon (Dragão)                                       =
    [17] Dark (Sombrio)                                        =
    [18] Fairy (Fada)                                          =
    ============================================================
    \n
    ''')
    if usuario_teste.isnumeric() == True:
        if int(usuario_teste) > 18:
            print('Por favor, digite um número apresentado na lista')
        if int(usuario_teste) < 1:
            print('Por favor, digite um número apresentado na lista')
    else:
        print('Tente novamente, dessa vez digitando apenas números Inteiros')

    my_poke_dict = {
        '1': 'Normal',
        '2': 'Fire',
        '3': 'Water',
        '4': 'Grass',
        '5': 'Flying',
        '6': 'Fighting',
        '7': 'Poison',
        '8': 'Electric',
        '9': 'Ground',
        '10': 'Rock',
        '11': 'Psychic',
        '12': 'Ice',
        '13': 'Bug',
        '14': 'Ghost',
        '15': 'Steel',
        '16': 'Dragon',
        '17': 'Dark',
        '18': 'Fairy'
    }

    for key in my_poke_dict:
        if usuario_teste == key:
            type = my_poke_dict[key]
    return type



'''
Função get_data_api: 
iremos receber o valor das duas funções anteriores -> ( Lista de pokemons , Tipo de Pokémon)
retorna uma lista com o nome dos pokémon que tem o tipo escolhido em primeira posição na pokedex
'''
def get_data_api(list_pokemon, type):
    pokemon_list = []
    for pokemon in list_pokemon:
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
            'query': '{\n\tgetPokemon(pokemon: '+ pokemon + ' reverseFlavorTexts: true takeFlavorTexts: 1) {\n\t\tnum\n\t\tspecies\n\t\ttypes\n\t\tabilities { first second hidden }\n\t\tbaseStats { hp attack defense specialattack specialdefense speed }\n\t\tgender { male female }\n\t\theight\n\t\tweight\n\t\tflavorTexts { game flavor }\n\t\tevYields { hp attack defense specialattack specialdefense speed }\n\t\tisEggObtainable\n\t\tminimumHatchTime\n\t\tmaximumHatchTime\n\t\tlevellingRate\n\t\tsprite\n\t\tshinySprite\n\t\tbackSprite\n\t\tshinyBackSprite\n\t\tsmogonTier\n\t\tsmogonPage\n\t\tserebiiPage\n\t\tbulbapediaPage\n\t}\n}',
        }

        response = requests.post('https://graphqlpokemon.favware.tech/', headers=headers, json=json_data)
        json = response.json()
        try:
            if type == json['data']['getPokemon']['types'][0]:
                pokemon_list.append(pokemon)
        except KeyError:
            pass
    return pokemon_list


'''
Função save_csv
recebe o parâmetro api ( lista de nomes dos pokémons de determinado tipo )
e retorna um csv com o nome de todos os pokémons daquele tipo selecionado 
(Lembrando que o pokémon tem que constar na lista de requisição)
'''
def load_csv(api, type):
    with open(f'pokemons_{type}_list.csv', 'w', encoding='utf8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for nome in api:
            writer.writerow([nome])


def main():
    poke_name = get_pokemon_name()
    input = get_input()
    print(f'Então o seu tipo de pokémon favorito é {input}?! Pode deixar!')
    get_api = get_data_api(poke_name, input)
    print(f'Segue uma lista dos pokémon do tipo {input} que encontrei:')
    csv_save = load_csv(get_api, input)
if __name__ == '__main__':
    main()
