from ball import Ball
from cartesianpoints import CartPoint
from score import Score
import random
import time

# Represents a list of random colors
random_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# New score object taken from the Score class
score = Score()


print('Lets say you have a ball.\n')
# Time delay
time.sleep(1.3)
print('This ball has a cartesian point (x, y), a radius, and a color.\n')
time.sleep(2.2)

print('Now, I want you to create your own ball.')
time.sleep(1.3)
print('You will create new balls until your ball is the same as my ball.\n')
time.sleep(2.2)
print("Let's begin!")
time.sleep(1.3)

# Creates the computer (cpu's) ball
cpu_center_x = random.randint(-4, 4)
cpu_center_y = random.randint(-4, 4)
cpu_radius = random.randint(1, 10)
cpu_color_int = random.randint(0, 5)
cpu_color = random_colors[cpu_color_int]

cpu_center = CartPoint(cpu_center_x, cpu_center_y)
cpu_ball = Ball(cpu_center, cpu_radius, cpu_color)

# Runs forever until broken out of
while True:

  # User prompts
  user_center_x = input('What would you like the center of the ball to be? (x coordinate): ')
  user_center_y = input('What would you like the center of the ball to be? (y coordinate): ')
  user_radius = input('Now, choose a radius for your ball! ')
  user_color = input('What color would you like your ball to be? ')

  user_center = CartPoint(int(user_center_x), int(user_center_y))

  user_ball = Ball(user_center, int(user_radius), user_color)

  # checking if any parameters are correct
  if user_ball.same_center(cpu_ball) and user_ball.same_radius(cpu_ball) and user_ball.same_color(cpu_ball):
    break
  if user_ball.same_center(cpu_ball):
    print('Correct center!\n')
  elif user_center.same_x(cpu_center):
    print('Correct X coordinate!\n')
  elif user_center.same_y(cpu_center):
    print('Correct Y coordinate!\n')
  if user_ball.same_radius(cpu_ball):
    print('Correct radius!\n')
  if user_ball.same_color(cpu_ball):
    print('Correct color!\n')
  if not (user_ball.same_center(cpu_ball) or (user_center.same_x(cpu_center)) or (user_center.same_y(cpu_center)) or
          user_ball.same_radius(cpu_ball) or user_ball.same_color(cpu_ball)):
    print('None of these were correct!\n')
    score.score_up()

final_score = score.return_score()

print('You guessed correctly!\n')
print('Your final score is: ' + str(final_score))
