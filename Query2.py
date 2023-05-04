import sqlite3
from pymongo import MongoClient
import sys

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon with an attack greater than 150
find_attack_greater_150 = pokemonColl.find({ "attack": { "$gt": 150 } })
for doc in find_attack_greater_150:
    print(doc)