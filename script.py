from poke_api import get_pokemon_info
from pastebin_api import post_new_paste
from sys import argv

def main():
    # Get the search term from command line parameter
    pokemon_name = argv[1]

    # Fetch pokemon information from the poke API
    poke_dict = get_pokemon_info(pokemon_name)

    # If pokemon are fetched successfully
    if poke_dict:

        # Determine the title of the new PasteBin paste
        paste_title = get_paste_title(pokemon_name)

        # Determine the body text of the new PasteBin paste
        paste_body = get_paste_body(poke_dict)

        # Create the new PasteBin paste
        paste_url = post_new_paste(paste_title, paste_body, '10M')

        # Print the URL of the new PasteBin paste
        print(paste_url)

def get_paste_body(poke_dict):
    poke_list = [p['poke'] for p in poke_dict['results']]
    paste_body = '\n\n'.join(poke_list)
    return paste_body

def get_paste_title(pokemon_name):
    return f'Pokemon About {pokemon_name.capitalize()}s'

main()