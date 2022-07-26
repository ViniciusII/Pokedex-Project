Objetivo do Código:
 - Consumir uma API de Pokémon e retornar informações de determinados tipos de Pokémons

Funções:
 - get_pokemon_name()
   - Essa função é responsável por trazer a lista com o nome dos pokémons que serão passados para a API
     ele faz uma requisição em um endereço aonde pode ser encontrado o nome de vários pokémon, retornando assim
     uma lista com todos os nomes que ele encontrar.
 
 - get_input()
   - Essa função irá chamar um objeto da Classe ' print_input ' aonde podemos encontrar a nossa tela de interação
     com o usuário, essa função retornará a String de um dos 18 tipos de pokémon que o Usuário escolheu.

 - get_data_api()
   - é aqui que a mágica acontece! Essa função é responsável por executar a API do Pokémon, ela receberá dois parâmetros
     a lista com o nome de todos os pokémons e o tipo que o Usuário selecionou, assim que encontrar um pokémon com o tipo
     selecionado, ele irá trazer o json com as informações e criar um dicionário com os status sobre os pokémon listados. 
     essa função retornará a lista com o dicionário de informações do Pokémon

 - get_response()
   - Essa função é utilizada para testarmos se o response das requisições retornará o status_code 200 

 - load_csv()
   - Essa função será responsável por salvar e escrever um arquivo CSV com os itens selecionados na API
     ela irá escrever uma nova linha para cada pokémon, com todos os status encontrados no json


Author: Vinicius Gomes Ribeiro
-26/07/2022