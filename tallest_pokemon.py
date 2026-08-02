import requests
import json

base_url = "https://pokeapi.co/api/v2/"

list_response = requests.get(f"{base_url}pokemon", params={"limit": 200})
list_data = list_response.json()

tallest = None
tallest_height = -1

for pokemon in list_data["results"]:
    detail_response = requests.get(pokemon["url"])
    detail_info = detail_response.json()

    if detail_info["height"] > tallest_height:
        tallest = detail_info["name"]
        tallest_height = detail_info["height"]


print(f"The tallest pokemon is: {tallest}, with a height of {tallest_height}")