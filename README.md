# python_classes
Lesson: Python Classes and Inheritance


## `2` Fighter

```py
# Create a class: Fighter
# Instance method (self, name, signature_move)
# 3 methods with your Fighter class (decide what those should be)

class Fighter():
    def __init__(self, name, signature_move):
        self.name = name
        self.signature_move = signature_move
        self.moves = [signature_move]
        self.power = 100
    
    def add_move(self, new_move):
        self.moves.append(new_move)

    def attack(self, move):
        if move in self.signature_move:
            print('Inside of condition 1')
            # return '{} is using Signature Move: {}'.format(self.name, self.signature_move)
            return f'{self.name} is using Signature Move: {self.signature_move}'
        elif move in self.moves:
            return 'Attack with {}'.format(move)
        else:
            return 'Please add move to fighter in order to use it'

    def list_moves(self):
        return self.moves


scorpion = Fighter('Scorpion', 'Spear Throw')
# Check some properties
print('# Check some properties')
print('Name', scorpion.name)
print('Signature Move', scorpion.signature_move)
print('All moves', scorpion.moves)
print('----')

print('# Run add_move method')
scorpion.add_move('Summon Flame')
scorpion.add_move('Weapon Attack 1')
print('All moves:', scorpion.list_moves())
print('-----')

print('# Run attack method')
print('Move 1 ->', scorpion.attack('Spear Throw')) # return a string, which has to be printed
print('Move 2 -> ', scorpion.attack('Summon Flame'))
print('Move 3 ->', scorpion.attack('Sumo Kick'))
```