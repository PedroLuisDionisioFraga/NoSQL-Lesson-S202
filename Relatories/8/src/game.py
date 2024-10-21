from database import Database

class Game:
  def __init__(self, database: Database):
    self.database = database

  def create_player(self, name: str, id: int):
    query = "CREATE (player:Player {name: $name, id: $id})"
    parameters = {"name": name, "id": id}
    self.database.execute_query(query, parameters)

  def delete_player(self, id: int):
    query = "MATCH (player:Player {id: $id}) DETACH DELETE player"
    parameters = {"id": id}
    self.database.execute_query(query, parameters)

  def update_player(self, name: str, id: int):
    query = "MATCH (player:Player {id: $id}) SET player.name = $name"
    parameters = {"name": name, "id": id}
    self.database.execute_query(query, parameters)

  def get_player(self, id: int):
    query = "MATCH (player:Player {id: $id}) RETURN player"
    parameters = {"id": id}
    return self.database.execute_query(query, parameters)

  def create_match(self, id: int):
    query = "CREATE (match:Match {id: $id})"
    parameters = {"id": id}
    self.database.execute_query(query, parameters)

  def delete_match(self, id: int):
    query = "MATCH (match:Match {id: $id}) DETACH DELETE match"
    parameters = {"id": id}
    self.database.execute_query(query, parameters)

  def update_match(self, id: int):
    query = "MATCH (match:Match {id: $id}) SET match.id = $id"
    parameters = {"id": id}
    self.database.execute_query(query, parameters)

  def get_match_winner(self, id: int):
    query = "MATCH (player:Player)-[r:PLAYED_IN {win: true}]->(match:Match {id: $id}) RETURN player"
    parameters = {"id": id}
    return self.database.execute_query(query, parameters)

  def get_player_matches(self, id: int):
    query = "MATCH (player:Player {id: $id})-[r:PLAYED_IN]->(match:Match) RETURN match"
    parameters = {"id": id}
    return self.database.execute_query(query, parameters)

  def create_player_match_relationship(self, player_id: int, match_id: int, win: bool):
    query = "MATCH (player:Player {id: $player_id}), (match:Match {id: $match_id}) CREATE (player)-[r:PLAYED_IN {win: $win}]->(match)"
    parameters = {"player_id": player_id, "match_id": match_id, "win": win}
    self.database.execute_query(query, parameters)
