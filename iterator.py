# iterator

scores = [40, 50, 70, 90, 60]
# it = iter(scores) # it become iterator
# print(next(it)) # next is pulling the data from next
# print(next(it))
# print('hello')
# print(next(it))
#
# for score in scores:
#         print(score)    # automatically converts to iterator

def get_infinite(): #generator
    i = 0
    while True:
        yield i * 2
        i += 1

g = get_infinite()
print(next(g))
print(next(g))
print(next(g))
