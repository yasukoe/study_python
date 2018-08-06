# function

# def say_hi():
#     print('hi')
#
# say_hi()

# def say_hi(name, age = 20):
#     print('hi {0} ({1})'.format(name, age))
#
# say_hi('Tom', 23) #Tom (23)
# say_hi('Jon', 30) #Jon (30)
# say_hi('Steve') #Steve (20)
# say_hi(age = 18, name = 'Bob')

def say_hi():
    return 'hi'

test=say_hi()
print(test)

def say_hi2():
    pass

msg=say_hi2()
print(msg) # retun as None
