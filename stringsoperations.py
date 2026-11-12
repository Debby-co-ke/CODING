string1 = 'Hello'
string2 = "World"

# Concatenation
combined = string1 + " " + string2
print("Concatenated String:", combined)

string3 = "123456789"

x = int(string3) # Convert string to integer
y = x + 10
print("Converted Integer plus 10:", y)

#reading user input
# usename = input("Enter your name: ")
# password = input("Enter your password: ")

# print("Username:", usename)
# print("Password:", password)

#looking inside the string
fruit = "banana"
letter = fruit[4]
print("Second letter of fruit:", letter)


#length of the string
toy = "Truck"
print("Length of toy string:", len(toy))


#interation of the fruit string
Index = 0
while Index < len(fruit):
    letter = fruit[Index]
    print("Letter at index", Index, "is", letter)
    Index = Index + 1

#using the for loop to iterate through the string
for letter in fruit:
    print("Letter in fruit using for loop:", letter)


#counting occurrences of a letter in a string
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print("Number of 'a' in fruit:", count)

#Slicing the string
fullname = "John Doe"
first_name = fullname[0:4]
last_name = fullname[5:8]
print("First Name:", first_name)
print("Last Name:", last_name)

#using the in logical operator
house = "My house is big"
has_big = "big" in house
print("Does the house string contain 'big'?", has_big)
has_small = "small" in house
print("Does the house string contain 'small'?", has_small)

#string comparison
str1 = "apple"
str2 = "banana"
is_equal = str1 == str2
is_greater = str1 > str2
print("Are the strings equal?", is_equal)
print("Is str1 greater than str2?", is_greater)


#string methods
#converting strings to lower case
program = "BSC YR TWO"
university_program = program.lower()
print("Lowercase program string:", university_program)

#converting strings to upper case
course = "computer science"
university_course = course.upper()
print("Uppercase course string:", university_course)

#REPLACING parts of a string
text = "I like cats"
new_text = text.replace("cats", "dogs")
print("Replaced text:", new_text)

#finding a substring in a string
sentence = "The quick brown fox jumps over the lazy dog"
position = sentence.find("fox")
print("Position of 'fox' in sentence:", position)
not_position = sentence.find("cat")
print("Position of 'cat' in sentence (not found):", not_position)

#stripping whitespace from a string
greet = "   Hello, World!   "
stripped_greet = greet.strip()
print("Stripped greeting:", "'" + stripped_greet + "'")
