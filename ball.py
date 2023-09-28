from cartesianpoints import CartPoint
import math

# represents a ball class
class Ball:
  def __init__(self, center, radius, color):
    self.center = center
    self.radius = radius
    self.color = color

  # returns the area of the ball
  # (uneeded for this but good practice)
  def area(self):
    return math.pi * (self.radius ** 2)

  # returns the circumference of the ball
  # (uneeded for this but good practice)
  def circumference(self):
    return 2 * math.pi * self.radius

  # checks equality with all parameters of the ball
  def same_center(self, other):
    return self.center.check_equality(other.center)
    
  def same_radius(self, other):
    return self.radius == other.radius
    
  def same_color(self, other):
    return self.color == other.color

# one example of a ball (unused in the actual game)
ball_example = Ball(CartPoint(1, 2), 2, 'blue')
ball_example_2 = Ball(CartPoint(1, 2), 3, 'yellow')















