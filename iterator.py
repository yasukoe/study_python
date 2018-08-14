# iterator
''' absic knowledge '''

scores = [40, 50, 70, 90, 60]
# it = iter(scores) # it become iterator
# print(next(it)) # next is pulling the data from next
# print(next(it))
# print('hello')
# print(next(it))
#
# for score in scores:
#         print(score)    # automatically converts to iterator

def get_infinite(): #generator if yield includes
    i = 0
    while True:
        yield i * 2
        i += 1

g = get_infinite()
print(next(g))
print(next(g))
print(next(g))

# another example
def myfunc():
    yield 'one'
    yield 'two'
    yield 'three'

for i in myfunc():
    print(i)

#Below is the same result with above
# i = myfunc()
# print(next(i))
# print(next(i))
# print(next(i))

''' using map()
    map(function, itelator)
'''

def triple(n):
    return n*3

#for using print, you need to use list function to execute print function
# because map return the generator
print(list(map(triple, [1,2,3])))

''' using lambda
    lambda argument: manipulate(argument)
    Lambdas are one line functions.
'''
print(list(map(lambda n: n*3, [1,2,3])))

add = lambda x, y: x + y
print(add(3,5))

#list sorting
a = [(1,2),(4,1),(9,10),(13,-3)]
a.sort(key=lambda x: x[1])
print(a) #[(1, 2), (4, 1), (9, 10), (13, -3)]

''' filter
    filter(function, itelator)
'''
def is_even(n): #Only even numbers return
    return n%2 ==0

print(list(filter(is_even, range(10))))

print(list(filter(lambda n: n%2 == 0, range(10))))

ages = [3,16,15,30,45,44]
def f(x):
    if x < 20:
        return False
    else:
        return True
# adults = filter(f,ages)
# for i in adults:
#     print(i)
print(list(filter(f,ages)))
