# concat

a = 'hello'
b = 'hi'
c = a+b

# Using in as a Logical Operator

fruit = 'banana'
'n' in fruit #True
'm' in fruit #False
'nan' in fruit #True
if 'a' in fruit :
    print('Found it')


# String Comparison

word = 'banana'

if word == 'banana' :
    print('All right, bananas.')

if word < 'banana':
    print('your word, ' + word + ', comes before banana')
elif word > 'banana':
    print('your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# String library

'''
built into every string
don't modify the original string, return new string
.capitalize()
.center(width[, fillchar])
.endswith
.find
.lstrip
.replace
.lower
.rstrip
.strip
.upper 등등 많은 library가 이미 내장됨.
'''
#ex1) lower
gree = 'hello'
print(gree)
print(gree.lower())
print('hello'.lower())

stuff = 'Hello world'
type(stuff) # <class 'str'>
dir(stuff) # ['lower', 'isupper', ...] methods of class 'str'

#ex2) find
fruit = 'banana'
pos = fruit.find('nana')
print(pos) #2
print(fruit.find('hello')) #-1

#ex3) replace : search and replace

greet = 'hello bob'
print(greet.replace('bob', 'jane'))
print(greet.replace('o', 'x'))#hellx bxb

#ex4) stripping whitespace

greet ='    Hello Bob   '
greet.lstrip() #'Hello Bob   '
greet.rstrip()
greet.strip() #'Hello Bob'

#ex5) startswith : prefixes return True/False

line = 'please have a nice day'
line.startswith('please') #True
line.startswith('P') #False

# Parsing and Extracting

data = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008'
atpos = data.find('@')
print(atpos) #21
sppos = data.find(' ',atpos) #atpos 이후의 최초 ' '을 find
print(sppos) #31
host = data[atpos+1 : sppos] #atpos+1과 sppos 사이의 문자열
print(host) 

# Strings and Character Sets

'''
python 2 : unicode type이 존재
python 3 : 모든 string이 unicode이므로, 모든 type을 str로 표기
'''

x = u'창현'
type(x) # python2 : <type 'unicode'> python3 : <type 'str'>

print('hello'[1:3])