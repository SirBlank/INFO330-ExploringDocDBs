import sqlite3
from pymongo import MongoClient
import sys

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon with an ability of "Overgrow"
find_ability_overgrow = pokemonColl.find({ "abilities": { "$regex": ".*Overgrow.*" } })
for doc in find_ability_overgrow:
    print(doc)