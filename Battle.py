import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])

    p1_stat = 0
    p2_stat = 0
    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            p1_stat += 1
            print(pokemon1['name'] + " has the advantage in " + stat)
        elif pokemon2[stat] > pokemon1[stat]:
            p2_stat += 1
            print(pokemon2['name'] + "'s " + stat + " is superior")
        else:
            print(pokemon1['name'] + "'s " + stat + " and " + pokemon2['name'] + "'s " + stat + " is the same!")

    if p1_stat > p2_stat:
        print(pokemon1['name'] + " wins with " + str(p1_stat) + " stats!")
    elif p2_stat > p1_stat:
        print(pokemon2['name'] + " wins with " + str(p2_stat) + " stats!")
    else:
        print("The battle is a tie!")

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
