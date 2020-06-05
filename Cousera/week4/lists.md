## collections : more than one value in variable
  - tuple
  - list
  - dictionary

## not a collection?

    - variable has one value
    - when we put a new value in the variable, the old value is overwritten

## List is a kind of collection

    collection : allows us to put many values in a single variable
    
    friends = ['a', 'b', 'c']
    
## List constants

list element can be any Python object - even another list
 
[1, 'hello', [1,2,3]]

## Lists are mutable(can change an element)

fruit = 'banana'
fruit[0] = 'B' *error 발생

lotto = [2,1,4,2,1]
lotto[2] = 23
print(lotto) *mutable

## How long is a list?

```py
x = [1,2,'joe', 00]
print(len(x)) #4
```

## Using the Range Function

```py
print(range(4))
#[0,1,2,3]
frineds = ['a', 'b', 'c', 'd']
print(len(frineds)) #4
print(range(len(friends))) #[0,1,2,3]
```
