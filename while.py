# [while]

i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
else:
    print('end')

'''
[for]
for variable in range of data
   operate
for i in range(0,10): # 0 to 9
'''
for i in range(10): # 0 to 9
    if i==5:
        # break
        continue # not print 5 as there is no print here
    print(i)
else:
    print('end')
