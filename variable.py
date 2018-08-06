# function
# msg = 'Hello'
# def say_hi():
#      msg = 'hi' #Local variable - this variable scope is in this function
#      print(msg)
#
# say_hi()
# print(msg) #Hello

msg = 'Hello from global'
def say_hi():
    global msg #this means below variable set as global
    msg = 'Hello global'
    print(msg) #Hello from global
say_hi()
print(msg)
