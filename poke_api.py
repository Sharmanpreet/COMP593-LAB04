import requests

URL = 'https://pokeapi.co/api/v2/'

def get_pokemon_info(pokemon_name='', pokemon_id=1, pokemon_abilities= 0):
    """
    Fetches Pokemons from the Poke API that contains specified pokemon.
    
    :param pokemon_name: Pokemon name to use (Empty string = list all pokemons)
    :param pokemon_id: The identifier for pokemon.
    :param pokemon_abilities: A list of abilities that were introduced in this generation
    :returns: Dictonary of pokemon, if successful. Otherwise None.
    """ 
     # List of Pokemon
    pokemon_name = str(pokemon_name).strip().lower()

    print(f'Searching for pokemons that contain {pokemon_name}...', end='')

    # name - Description
    # id - The identifier for this resource
    # abilities - A list of abilities that were introduced in this generation
    n = {
        'name': 'pokemon_name',
        'id': 'pokemon_id',
        'abilities': 'pokemon_abilities'
    }

    search_url = URL + 'search'
    resp_msg = requests.get(search_url)
    
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        
    else:
        print('failure')
        print(f'Status code: {resp_msg.status_code}, Error reason: {resp_msg.reason}')

