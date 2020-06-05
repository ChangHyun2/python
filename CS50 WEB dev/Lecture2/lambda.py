people = [
    {'name' : 'harry', 'house': 'gryffindor'},
    {'name' : 'cho', 'house': 'ravenclaw'},
    {'name' : 'draco', 'house': 'slytherin'}
] # dictionaries in list

'''
def f(person):
    return person['name']

people.sort(key=f) # dictionary끼리 < 로 비교하는 것이 불가능해 error ㅠ 
'''


people.sort(key=lambda person: person["name"]) 
# lamdba 함수명: return value
print(people)