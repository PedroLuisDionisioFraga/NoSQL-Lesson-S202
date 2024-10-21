from neo4j import GraphDatabase


class Database:
  def __init__(self, uri, user, password, database):
    self.driver = GraphDatabase.driver(uri, auth=(user, password))
    self.database = database

  def close(self):
    self.driver.close()

  def execute_query(self, query, parameters=None):
    data = []
    with self.driver.session(database=self.database) as session:
      results = session.run(query, parameters)
      for record in results:
        data.append(record)
      return data

  def drop_all(self):
    with self.driver.session() as session:
      session.run("MATCH (n) DETACH DELETE n")
