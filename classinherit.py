# class inherited
# User -> AdminUser

# class User:
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print('hi {0}'.format(self.name))
#
# class AdminUser(User):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#     def say_hello(self):
#         print('hi {0} ({1})'.format(self.name, self.age))
#
# bob = AdminUser('Bob', 23)
# print(bob.name)
# bob.say_hi()
# bob.say_hello()

# class mulple inherited
# A,B -> C

class A:
    def say_a(self):
        print("hi fromA!")
    def say_hi(self):
        print("hi fromA!")
class B:
    def say_b(self):
        print('B!')
    def say_hi(self):
        print("hi fromB!")
class C(A,B):
    pass

c=C()
c.say_a()
c.say_b()
c.say_hi() # A's show as class C(A,B):. if you want to show B's, change to C(B,A)
