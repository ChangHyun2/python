# Using open()

# handle = open(filename, mode)
fhand = open('test.txt', 'r') # 'r' & 'w'
fhand2 = open('test.txt')

print(fhand)
print(fhand2)

# newLine cgaracter

stuff = 'h\ni'
print(stuff, len(stuff))

# File processing
'''
a text file has newlines at the end of each line
a text file can be thought of as a sequence of lines
'''

# File handle as a sequence

for line in fhand:
    print(line)
    #remember : sequence is an ordered set

# Counting lines in a file

count = 0
for line in fhand2:
    count=count+1
print('line count:', count)

# Reading the whole file

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])