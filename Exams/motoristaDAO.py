from bson.objectid import ObjectId
from motorista import Driver
from db import Database
from motorista import Driver

class MotoristaDAO:
  def __init__(self, database: Database):
      self.db = database

  def create(self, motorista: Driver):
    try:
      res = self.db.collection.insert_one(vars(motorista))
      print(f"Created driver with ID: {res.inserted_id}")
      return res.inserted_id
    except Exception as e:
      print(f"An error occurred while creating motorista: {e}")
      return None

  def read(self, id: str):
    try:
      res = self.db.collection.find_one({"_id": ObjectId(id)})
      print(f"Driver found!!")
      return res
    except Exception as e:
      print(f"An error occurred while reading motorista: {e}")
      return None

  def update(self, id: str):
    try:
      driver = self.db.collection.find_one({"id": ObjectId(id)})
      rating = [i["rating"] for i in driver["corridas"]]
      rating_final = sum(rating) / len(rating)
      driver["rating"] = rating_final

      res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": driver})
      print(f"Driver updated: {res.modified_count} document(s) modified")
      return res.modified_count
    except Exception as e:
      print(f"An error occurred while updating motorista: {e}")
      return None

  def delete(self, id: str):
    try:
      res = self.db.collection.delete_one({"id": ObjectId(id)})
      print(f"motorista deleted: {res.deleted_count} document(s) deleted")
      return res.deleted_count
    except Exception as e:
      print(f"An error occurred while deleting motorista: {e}")
      return None
