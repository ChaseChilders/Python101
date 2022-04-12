# def print_pokemon(poke):
#   print(f"""
#   Pokemon {poke["number"]}: {poke["name"]}
#   Type/s: {poke["types"]}
#   poke["blurb]
#   """)

# pokemon = [
#   {
#     "name": "bulbasaur",
#     "number": "001",
#     "types": ["grass", "poison"],
#     "gender": "f",
#     "evolves_to": "TBD",
#     "blurb": "bulb lookin dude",
#     "height": 7,
#     "weight": 69,
#     "evolution_level": 16,
#     "evolves_to": ["ivysaur"]
#   }
#   {
#     "name": "evee",
#     "number": "070"
#     "types": ["grass", "poison"],
#     "gender": "f",
#     "evolves_to": "TBD",
#     "blurb": "bulb lookin dude",
#     "height": 7,
#     "weight": 69,
#     "evolution_level": 16,
#     "evolves_to": ["vaporeon", "flareon", "jolteon"]
#   }
# ]

# print_pokemon(pokemon[1])
def print_players(player):
  print(f"""
  Name: {player["name"]}
  Weight: {player["weight"]}
  Height: {player["height"]}
  Number: {player["number"]}
  Positions: {player["positions"]}
  Year Drafted: {player["year_drafted"]}
  """)
cowboys_players = [
  {
    "name": "Dak Prescott",
    "weight": "238 lbs",
    "height": "6'2",
    "number": 4,
    "positions":["QB"],
    "year_drafted": 2016
  },
  {
    "name": "Ezekiel Elliot",
    "weight": "228 lbs",
    "height": "6'0",
    "number": 21,
    "positions":["RB"],
    "year_drafted": 2016
  },
  {
    "name": "Tony Pollard",
    "weight": "209 lbs",
    "height": "6'0",
    "number": 20,
    "positions":["RB"],
    "year_drafted": 2019
  },
  {
    "name": "Cee Dee Lamb",
    "weight": "200 lbs",
    "height": "6'2",
    "number": 88,
    "positions":["WR"],
    "year_drafted": 2020
  },
  {
    "name": "Dalton Shultz",
    "weight": "244 lbs",
    "height": "6'5",
    "number": 86,
    "positions":["TE"],
    "year_drafted": 2018
  }]
  # {
  #   "name":
  #   "weight":
  #   "height":
  #   "number":
  #   "positions":[]
  #   "year_drafted":
  # }

print_players(cowboys_players[1])