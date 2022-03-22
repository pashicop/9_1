from pprint import pprint

import requests

def get_id(name):
    req = "https://superheroapi.com/api/2619421814940190/search/" + name
    response = requests.get(req)
    response.raise_for_status()
    json_dict = response.json()
    results = json_dict["results"]
    for result in results:
        if result["name"] == name:
            id = result["id"]
            break
    return id

def get_intelligence(id):
    req = "https://superheroapi.com/api/2619421814940190/" + id
    response = requests.get(req)
    response.raise_for_status()
    json_dict = response.json()
    intelligence = int(json_dict["powerstats"]["intelligence"])
    return intelligence

if __name__ == '__main__':
    list_superhero = ["Hulk", "Captain America", "Thanos"]
    final_intelligence = 0
    for hero in list_superhero:
        current_intelligence = get_intelligence(get_id(hero))
        if current_intelligence > final_intelligence:
            final_intelligence = current_intelligence
            winner = hero
    print(f'Победитель – {winner}')