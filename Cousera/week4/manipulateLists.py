## lists can be sliced using :

t = [1,2,3,1,23,2,12,4]
t[1:3]
t[3:]
t[:] # == t

## list methods

x = list()
type(x)

dir(x)
# append count extend index insert pop remove reverse sort

## is something in a list?
names = ['a', 'b', 'c']
0 in names ## false
'a' in names ## true
0 not in names ## true

## lists are in order

names.sort() # sort yourself
print(names)
print(names[1])

## built-in functions and lists

nums = [3,2,4,2,5,12,1,2]
print(max(names))
print(min(names))
print(sum(names)/len(names))

## get average in differnt ways

# average using varaibles
total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print(average)

# average using list : 입력 개수에 따라 차지하는 memory 공간이 증가함
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print(average)
 