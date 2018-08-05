''' this file is for studing 'strings' '''
print('Hello HiFiWidow')
# using variable
msg = 'Hello HiFiwidow'
print(msg)

# using comment for inserting strings
msg = """
test_1
test_2
"""
print(msg)

#using += to add more values
msg = 'Python'
msg += "-"
msg += "commit"
print(msg)

#increment the values -> 012012012
msg = '012'*3
print(msg)

#change the number to strings
int = 100
print(str(int) + 'yen')

#replace the values
msg = 'HiFiWidow'
print(msg.replace('HiFi','Python'))

#aplit the strings
msg = 'HiFi-Widow'
print(msg.split('-'))

#right-justified with filling the specified spaces
msg = '1234'
print(msg.rjust(10,'0'))
print(msg.rjust(10,'!'))

#filling by zero
print(msg.zfill(10))
print(msg.zfill(3))

#start from startswith
msg = 'LearningPython'
print(msg.startswith('Python'))
print(msg.startswith('Learning'))
