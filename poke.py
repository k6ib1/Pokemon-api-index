import json
import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    print(f"Failed to retrieve data: {response.status_code}")
    return None


pokemon_name = input("Enter a pokemon name: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    with open("pokemon.json", "w", encoding="utf-8") as file:
        json.dump(pokemon_info, file, indent=2)

    print("\nSaved response to pokemon.json")

    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")





