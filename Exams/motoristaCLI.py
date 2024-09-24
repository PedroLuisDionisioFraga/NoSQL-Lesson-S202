from motoristaDAO import MotoristaDAO
from corrida import Race
from passageiro import Passenger
from motorista import Driver

class SimpleCLI:
  def __init__(self):
    self.commands = {}

  def add_command(self, name, function):
    self.commands[name] = function

  def run(self):
    while True:
      command = input("Enter a command: ")
      if command == "quit":
        print("Goodbye!")
        break
      elif command in self.commands:
        self.commands[command]()
      else:
        print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):

  def __init__(self, driver_DAO: MotoristaDAO):
    super().__init__()
    self.driver_DAO = driver_DAO
    self.add_command("create", self.create)
    self.add_command("read", self.read)
    self.add_command("update", self.update)
    self.add_command("delete", self.delete)

  def run(self):
    print("Welcome to Race!")
    print("Use the follow commands:\n\tcreate\n\tread\n\tupdate\n\tdelete\n\tquit")
    super().run()

  def create(self):
    final_rating = 0
    # Creating a passenger
    name = input("Enter the passenger's name: ")
    document = input("Enter the passenger's document: ")
    passenger = Passenger(name, document)

    races = []
    race_size = int(input("Enter the number of rides (1 or more): "))
    for i in range(race_size):
      rating = int(input("Enter the ride rating (1 to 10): "))
      final_rating += rating
      distance = float(input("Enter the distance traveled: "))
      value = float(input("Enter the ride value: "))

      act_race = Race(rating, distance, value, passenger.dict())
      races.append(vars(act_race))

    driver = Driver(races, final_rating / race_size)
    self.driver_DAO.create(driver)
    print("Driver successfully registered.")

  def update(self):
    id = input("Enter the ID: ")
    self.driver_DAO.update(id)

    name = input("Enter the passenger's name: ")
    document = input("Enter the passenger's document: ")
    passenger = Race(name, document)

    races = []
    races_size = int(input("Enter the number of rides (1 or more): "))
    for i in range(races_size):
      rating = int(input("Enter the ride rating: "))
      distance = float(input("Enter the distance traveled: "))
      value = float(input("Enter the ride value: "))

      act_race = Race(rating, distance, value, passenger.dict())
      races.append(vars(act_race))

    self.driver_DAO.update(id)
    print("Driver successfully updated.")

  def read(self):
    id = input("Enter the ID: ")
    driver = self.driver_DAO.read(id)

    if driver:
      print(f"Total Ride Rating: {driver['rating']}")
      for race in driver["races"]:
        print(f"-----------------------------------------------")
        print(f"Rating: {race['rating']}")
        print(f"Distance: {race['distance']}")
        print(f"Value: {race['value']}")
        print(f"Passenger Name: {race['passenger']['name']}")
        print(f"Passenger Document: {race['passenger']['document']}")
        print(f"-----------------------------------------------")
    else:
      print("Driver not found!!")

  def delete(self):
    id = input("Enter the ID: ")
    self.driver_DAO.delete(id)
    print("Driver successfully deleted.")
