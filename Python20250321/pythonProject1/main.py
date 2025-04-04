class Player:
  def __init__(self, health):
    self.__health = health

  @property
  def health(self):
    return self.__health

  @health.setter
  def health(self, health):
    if 0 < health < 100:
      self.__health = health
    else:
      print("Error")

p = Player(500)
print(p.health)
p.health = 101
print(p.health)
