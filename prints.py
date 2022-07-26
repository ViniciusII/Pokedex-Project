class print_input:
    def __init__(self):
        pass

    def print_input(self):
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
            ''').strip()
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