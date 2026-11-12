# Data Structures Module
#List Data Structure
my_list = [1, 2, 3, 4, 2, 2, 2, 5]
print("Original List:", my_list)

#Adding an element to the list
my_list.append(6)
print("List after appending 6:", my_list)

#Using while loop to iterate through the list
my_list_index = 0
while my_list_index < len(my_list):
    print("Element at index", my_list_index, "is", my_list[my_list_index])
    my_list_index += 1

#Accessing elements in the list
my_list_element = my_list[2]

print("Element at index 2:", my_list_element)

#Removing an element from the list
my_list.remove(3)
print("List after removing 3:", my_list)

#List of strings
string_list = ["apple", "banana", "cherry"]
print("String List:", string_list)

#adding a string to the list
string_list.append("date")
print("String List after appending 'date':", string_list)


#for loop to iterate through the string list
for fruit in string_list:
    print("Fruit in string list:", fruit)

#slicing the string using for loop
for fruit in string_list[1:3]:
    print("Sliced fruit in string list:", fruit)

#slicing the string list
sliced_list = string_list[1:3]
print("Sliced String List (index 1 to 2):", sliced_list)


#Accessing elements in the string list
string_element = string_list[0]
print("Element at index 1 in string list:", string_element)

#Removing a string from the list
string_list.remove("banana")
print("String List after removing 'banana':", string_list)

#List of different data types
mixed_list = [1, "hello", 3.14, True]
print("Mixed List:", mixed_list)

#Adding an element to the mixed list
mixed_list.append(None)
print("Mixed List after appending None:", mixed_list)

#Tuple Data Structure
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)


#Counting occurrences of an element in the list
number_count = my_list.count(2)
print("Count of 2 in my_list:", number_count)


#Sorting the list
my_list.sort()
print("Sorted List:", my_list)



card = list()
card.append(9)
card.append(7)
card.append(56) 

print(card)