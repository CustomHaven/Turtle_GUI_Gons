import random

class Shapes:
  """Blueprint for drawing the Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon, and Decagon."""
  def __init__(self, max_size = 10, sides=3) -> None:
    self.r = random.randrange(1, 256)
    self.g = random.randrange(1, 256)
    self.b = random.randrange(1, 256)
    self.sides = sides
    self.track_turns = 0
    self.max_shape_size = max_size

  def get_colors(self):
    return (self.r, self.g, self.b)

  def change_color(self):
    """Changes the color and returns get_colors"""
    self.r = random.randrange(1, 256)
    self.g = random.randrange(1, 256)
    self.b = random.randrange(1, 256)
    return self.get_colors()
      
  def cal_angle(self) -> int:
    """Calculates the angle for the sides of the gon's"""
    return 360 / self.sides

  def increase_sides(self) -> None:
    """Increases the sides and restarts the number of turns"""
    self.sides += 1
    self.track_turns = 1
  
  def track_side_turns(self) -> bool:
    """Tracks the turns then changes the gon if max Decagon is reached stops the Shaping"""
    if self.sides == self.track_turns:
      if self.max_shape_size == self.sides:
        return False
      else:
        self.increase_sides()
        return True
    else:
      self.track_turns += 1
      return True