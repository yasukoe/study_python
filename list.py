# list is mutable and tuple is inmutable
# range type - no order no overlap allowed
# dictionaly type - using key to manage the data

# list
scores = [10, 20]
# print(scores[0]) # start from zero
# scores[0] = 45 # change value
# print(len(scores)) # 2 -  len is length
# print(scores)

# using for to show data

for score in scores:
    print(score)

# using enumerate
# enumerate() is to get the data with index number in for loop
for i, score in enumerate(scores):
    print("{0}: {1}". format(i, score))

# this is the sample if enumerate is not used
i=0
for score in scores:
    print("{0}: {1}". format(i, score))
    i+=1
