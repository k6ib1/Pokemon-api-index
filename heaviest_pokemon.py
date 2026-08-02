import json
import requests

base_url = "https://pokeapi.co/api/v2/"



list_response = requests.get(f"{base_url}pokemon", params={"limit": 1000})   # recieving first 1000 pokemon
list_data = list_response.json()

heaviest = None
heaviest_weight = -1

for pokemon in list_data["results"]:   
    detail_response = requests.get(pokemon["url"])   # each specific url for each pokemon is obtained
    pokemon_data = detail_response.json()            # and put in a dictionary

    weight = pokemon_data["weight"]

    if weight > heaviest_weight:
        heaviest_weight = weight
        heaviest_name = pokemon_data["name"]



print(f"The heaviest Pokémon is {heaviest_name} with weight {heaviest_weight}")

