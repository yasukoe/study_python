# function is called as method in class
class User:
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name
    #instance method
    def say_hi(self):
        print('hi {0}'.format(self.name))
    # class method - decorator
    @classmethod
    def show_info(cls):
        print('{0} instances'.format(cls.count))


tom = User('Tom')
bob = User('Bob')

tom.say_hi()
bob.say_hi()

User.show_info()
