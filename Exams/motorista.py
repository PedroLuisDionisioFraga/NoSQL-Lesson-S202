from typing import List
from corrida import Race

class Driver:
  def __init__(self, races: List[Race], rating: int):
    self.races = races
    self.rating = rating
