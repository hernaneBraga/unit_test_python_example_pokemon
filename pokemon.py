import requests

def get_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to retrieve data"
    

def compare_pokemons_height(poke1, poke2):
    if poke1['height'] > poke2['height']:
        return poke1['name']
    elif poke2['height'] > poke1['height']:
        return poke2['name']
    else:
        return 'Both Pokémon have the same height'