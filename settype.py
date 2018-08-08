# set type - no order and no overlap

a = set([5,4,8,5])
print(a) # {8,4,5}

a = {5,3,8,5}
print(a) # {8,3,5}

a.add(2)
a.remove(3)
print(a) # 8,2,5 - the reason why 5 is last, is not allowed overlap. 5 is overlapped.
print(len(a)) #3

a = {1,3,5,8}
b = {3,5,8,9}
print(a|b)
print(a&b)
print(a-b) #differences - numbers only a has
print(b-a)
