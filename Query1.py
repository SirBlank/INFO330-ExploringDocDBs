import sqlite3
from pymongo import MongoClient
import sys

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon named "Pikachu"
find_pikachu = pokemonColl.find({"name": "Pikachu"})
for doc in find_pikachu:
    print(doc)