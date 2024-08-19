from database import Database
from helper.writeAJson import writeAJson
from bson import json_util
import json

class Pokedex:
  def __init__(self, database: Database):
    self._database = database

  def get_pokemons_have_evolution(self):
    data = self._database
    pokemons = data.collection.find({"next_evolution": {"$exists": True}})

    writeAJson(pokemons, "pokemons_have_next_evolution")

  def get_pokemon_by_name(self, name):
    data = self._database
    pokemons = data.collection.find({"name": name})
    writeAJson(pokemons, "pokemons_by_name")

  def get_pokemons_by_type(self, types: list):
    data = self._database
    pokemons = data.collection.find({"type": {"$in": types}})
    writeAJson(pokemons, "pokemnos_by_type")

  def get_pokemons_just_one_weakness(self, weakness: str):
    data = self._database
    pokemons = data.collection.find({"weaknesses": {"$size": 1}})
    writeAJson(pokemons, "pokemons_with_just_one_weakness")

  def get_pokemons_avg_spawns_less_two(self):
      data = self._database
      pokemons = data.collection.find({"avg_spawns": {"$lt": 2}})

      writeAJson(pokemons, "pokemons_avg_spawns_less_two")
