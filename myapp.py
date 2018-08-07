## split the file > refer the file in the same directry
from user import AdminUser, User

# bob = user.AdminUser('Bob',23)
bob = AdminUser('Bob',23)
tom = User('Tom')

print(bob.name)
bob.say_hi()
bob.say_hello()
tom.say_hi()
