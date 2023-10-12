import requests

rq = requests.get('https://raw.githubusercontent.com/Biuni/PokemonGo-Pokedex/master/pokedex.json')
Pokemoni = rq.json()


def no_of_pokemons():
    pokemon_count = len(Pokemoni['pokemon'])
    print('V pokedexe sa nachadza:', pokemon_count, 'pokemonov')


def print_All_pokemons():
    pokemon_list = Pokemoni.get('pokemon')
    for pokemon in pokemon_list:
        name = pokemon.get('name')
        types = ' and '.join(pokemon.get('type'))
        height = pokemon.get('height')
        weight = pokemon.get('weight')
        print(f'Pokemon {name} of {types} type is {height} high with a weight of {weight}.')


def print_evolution_of_pokemons():
    pokemon_list = Pokemoni.get('pokemon', [])
    print('\n\n===========EVOLUCNY DIAGRAM ================\n')
    for pokemon in pokemon_list:
        evolution = pokemon.get('next_evolution', [])
        prevEvolution = pokemon.get('prev_evolution', [])
        name = pokemon.get('name')
        
        if evolution and prevEvolution == []:
            evolutions_str = f'{name} -> ' + ' -> '.join([evolvedName['name'] for evolvedName in evolution])
            print(evolutions_str)




no_of_pokemons()
print_All_pokemons()
print_evolution_of_pokemons()








