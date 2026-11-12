#Dictionaries and Sets in python

names = dict()

names['AIIM/00002/2025'] = 'JAMES'
names['AIIM/00003/2025'] = 'JOY'
names['AIIM/00004/2025'] = 'JACK'
names['AIIM/00005/2025'] = 'JILL'

#print(names)


#Accessing values in dictionary
print(names['AIIM/00003/2025'])

#Iterating through dictionary
for key in names:
    print(f'Key: {key} => Value: {names[key]}')

#Using get method to access values
print(names.get('AIIM/00004/2025'))

#Using setdefault method
names.setdefault('AIIM/00006/2025', 'JENNY')
print(names)

#Iterating through dictionary
for key in names:
    print(f'Key: {key} => Value: {names[key]}')

#Using pop method to remove a key-value pair
removed_value = names.pop('AIIM/00002/2025')
print(f'Removed Value: {removed_value}')
#Iterating through dictionary
for key in names:
    print(f'Key: {key} => Value: {names[key]}')

#Using popitem method to remove the last inserted key-value pair
last_item = names.popitem()
print(f'Removed Item: {last_item}')
#Iterating through dictionary
for key in names:
    print(f'Key: {key} => Value: {names[key]}')


#Sets Data Structure
Team_A = {'Alice', 'Bob', 'Charlie'}
Team_B = {'David', 'Eve', 'Frank'}
Team_C = {'Grace', 'Henry', 'Ivy'}

teams = set()
teams.add('Team_A')
teams.add('Team_B')
teams.add('Team_C')
teams.add('Team_A')  # Duplicate, will not be added to the set

print(teams)  # Output: {'Team_A', 'Team_B', 'Team_C'}

#Iterating through set
for team in teams:
    print(f'Team: {team}')

#Removing an element from set
teams.remove('Team_B')
print(teams)  # Output: {'Team_A', 'Team_C'}
for team in teams:
    print

#adding back removed element
teams.add('Team_B')
print(teams)  # Output: {'Team_A', 'Team_B', 'Team_C
for team in teams:
    print(f'Team: {team}')


#llooking for an element in set
if 'Team_C' in teams:
    print('Team_C is present in the set')
    
