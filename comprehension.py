# comprehension 内包表記

# print([i for i in range(10)])
# print([i*3 for i in range(10)])
# print([i*3 for i in range(10) if i % 2 ==0])

print(i*3 for i in range(10) if i % 2 ==0) #Generator
print({i*3 for i in range(10) if i % 2 ==0}) #set type
