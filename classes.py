# cup = {
#     "capacity": 12,
#     "color": "blue"
# }

# cup["capacity"]
# cup.get('color')


class CoffeeCup():
  def __init__(self, capacity):
    self.capacity = capacity
    self.amount = 0

  def fill(self):
      print('Fill coffee cup')
      self.amount = self.capacity

  def empty(self):
      self.amount = 0

  def drink(self, amount):
    self.amount -= amount
    if (self.amount <= 0):
        print('Cup is empty')
        self.amount = 0

# Made an instance
starbucks_cup = CoffeeCup(16)
print('Capacity', starbucks_cup.capacity) # 16
print('Amount', starbucks_cup.amount) # 0
print('------')
# Run the fill method
print('# Run the fill method')
starbucks_cup.fill()
print('Amount', starbucks_cup.amount) # 16
print('------')

# Run the drink method
print('# Run the drink method')
starbucks_cup.drink(8)
print('New amount', starbucks_cup.amount)
print('------')

# Run the empty method
print('# Run the empty method')
starbucks_cup.empty()
print('Amount', starbucks_cup.amount) # 0

# Run the fill method
print('# Run the fill method')
starbucks_cup.fill()
print('Amount', starbucks_cup.amount) # 16
print('------')

# Create a class: Fighter
# Instance method (self, name, signature_move)
# 3 methods with your Fighter class (decide what those should be)