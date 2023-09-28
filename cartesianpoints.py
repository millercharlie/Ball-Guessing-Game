# represents a cartesian point
class CartPoint:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # prints itself (uneeded for this but good practice)
  def print_self(self):
    print('My coordinates are: (' + self.x + ', ' + self.y + ')')

  # checks the equality of x and y
  def check_equality(self, other):
    return (self.x == other.x) and (self.y == other.y)

  # checks the equality of x
  
  def same_x(self, other):
    return self.x == other.x

  # checks the equality of y
  def same_y(self, other):
    return self.y == other.y
