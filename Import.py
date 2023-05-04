import sqlite3
from pymongo import MongoClient
import sys

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Connect to SQLite database
connection = sqlite3.connect("pokemon.sqlite")
try: 
    cursor = connection.cursor()

    # Execute query to retrieve data from SQLite
    query = """
            SELECT 
            pokemon.id,
            pokemon.name,
            pokemon.pokedex_number,
            GROUP_CONCAT(type.name, ', ') AS type_names,
            pokemon.hp,
            pokemon.attack,
            pokemon.defense,
            pokemon.speed,
            pokemon.sp_attack,
            pokemon.sp_defense,
            replace(GROUP_CONCAT(DISTINCT ability.name), ',', ', ')
            FROM pokemon
            JOIN pokemon_abilities ON pokemon.id = pokemon_abilities.pokemon_id
            JOIN ability ON pokemon_abilities.ability_id = ability.id
            JOIN pokemon_type ON pokemon.id = pokemon_type.pokemon_id
            JOIN type ON pokemon_type.type_id = type.id
            GROUP BY pokemon.id
            """
    cursor.execute(query)
    data = cursor.fetchall()

    for row in data:
        doc = {}
        doc["_id"] = row[0]
        doc["name"] = row[1]
        doc["pokedex_number"] = row[2]
        doc["types"] = row[3]
        doc["hp"] = row[4]
        doc["attack"] = row[5]
        doc["defense"] = row[6]
        doc["speed"] = row[7]
        doc["sp_attack"] = row[8]
        doc["sp_defense"] = row[9]
        doc["abilities"] = row[10]
        pokemonColl.insert_one(doc)

# Close connections
finally:
    cursor.close()
    connection.close()
    mongoClient.close()