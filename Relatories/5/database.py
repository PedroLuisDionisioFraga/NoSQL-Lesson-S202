import pymongo

class Database:
  """
  Connects to a MongoDB database and manages the collection.
  """

  def __init__(self, database, collection):
    """
    Initializes the connection to the specified database and collection.
    """
    self.connect(database, collection)

  def connect(self, database, collection):
    """
    Establishes the connection to the MongoDB server.
    """
    try:
      connectionString = "localhost:27017"
      self.clusterConnection = pymongo.MongoClient(
        connectionString,
        tlsAllowInvalidCertificates=True
      )
      self.db = self.clusterConnection[database]
      self.collection = self.db[collection]
      print("Connected to the database successfully!")
    except Exception as e:
      print(e)

  def resetDatabase(self):
    """
    Resets the database by dropping the collection.
    """
    try:
      self.db.drop_collection(self.collection)
      print("Database reset successfully!")
    except Exception as e:
      print(e)
