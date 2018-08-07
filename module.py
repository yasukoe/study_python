# split the file

# from user import AdminUser
# from user import AdminUser, User
from mypackage.user import AdminUser, User

# bob = user.AdminUser('Bob',23)
# bob = mypackage.user.AdminUser('Bob',23)
bob = AdminUser('Bob',23)
# tom = mypackage.user.User('Tom')
tom = User('Tom')

print(bob.name)
bob.say_hi()
bob.say_hello()
tom.say_hi()
