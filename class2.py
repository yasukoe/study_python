
class User:
    # class variable
    count = 0
    def __init__(self, name, score, level):
        User.count += 1 #count belongs to User class
        self.name = name
        self.score = score
        self.level = level

print(User.count) # 0
tom = User('Tom', 20, 5)
print('Name is {0}, score is {1}, level is {2}'
 .format(tom.name, tom.score, tom.level))
bob = User('Bob', 30, 7)
print(User.count) # 2 as added two instance

print(tom.count) # 2
