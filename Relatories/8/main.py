from database import Database
from src.game import Game

url = "bolt://44.203.54.52"
username = "neo4j"
password = "exteriors-mondays-hoof"
database = "neo4j"

print(f"URI: {url}")
print(f"Username: {username}")
print(f"Password: {password}")
print(f"Database: {database}")

db = Database(url, username, password, database)
db.drop_all()

game = Game(db)

for i in range(10):
  game.create_player(f"Player {i}", i)

for i in range(5):
  game.create_match(i)

# creates relationships between players and matches (each match with 2 players)
# players 0, 1, 2, 3, and 4 won matches 0, 1, 2, 3, and 4, respectively
for i in range(5):
  game.create_player_match_relationship(i, i, True)

# players 5, 6, 7, 8, and 9 lost matches 0, 1, 2, 3, and 4, respectively
for i in range(5, 10):
  game.create_player_match_relationship(i, i - 5, False)

# retrieves the player who won each match
for i in range(5):
  result = game.get_match_winner(i)
  if result:
    print(f"Who won match: {result[0]['player']['name']}")
  else:
    print("Match not finished")

# retrieves the matches for each player
for i in range(10):
  result = game.get_player_matches(i)
  for record in result:
    print(f"Matches of player {i}: {record['match']['id']}")
