#Introduction to loops in python
# 1. For Loop
# 2. While Loop

# code syntax of for loop
# for variable in sequence:
#     # code block to be executed

for i in range(5):
    print("For Loop iteration:", i)

# code syntax of while loop
# while condition:
#     # code block to be executed

while_condition = 0
while while_condition < 5:
    print("While Loop iteration:", while_condition)
    while_condition += 1


# Example: Using loops to calculate the sum of first 10 natural numbers
sum_natural = 0
for num in range(1, 11):
    sum_natural += num
print("Sum of first 10 natural numbers:", sum_natural)

while_sum = 0
while num <= 10:
    while_sum += num
    num += 1
print("Sum of first 10 natural numbers using while loop:", while_sum)

#Loop Control Statements
# 1. Break Statement
# 2. Continue Statement
# 3. Pass Statement

# Example of Break Statement
for i in range(10):
    if i == 5:
        print("Break at:", i)
        break
    print("Looping:", i)

# Example of Continue Statement
for i in range(10):
    if i % 2 == 0:
        print("Continue at even number:", i)
        continue
    print("Odd number:", i)

# Example of Pass Statement
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print("Looping with pass statement:", i)