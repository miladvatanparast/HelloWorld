print("Hello, World!, This was Arithmetic and Variables")

print(1 + 2)
print(2 - 1)
print(2 * 2)
print(10 / 2)
print(2 ** 5)

#This is a comment

Test_var = 4 + 5
print(Test_var)

# Set the value of a new variable to 3
my_var = 3

# Print the my_var
print(my_var)

# Change the vaalue of my_var to 100
my_var = 100

# Print the ne value assigned to  my_var
print(my_var)

# Increase the value of my_var by 3
my_var = my_var + 3

# Print the new value of my_var which is increased by 3
print(my_var)

# Create variables
num_years = 4
days_per_year = 365
hours_per_day = 24
min_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = num_years * ( days_per_year * (hours_per_day * (min_per_hour * secs_per_min)) )

# Print total secs of 4 years
print(total_secs)

print("Functions Section")

# Define the function
def add_three(any_number):
    output_number = any_number + 3
    return output_number
# Run the number with 10 as input
new_number = add_three(10)

# Print the new number
print(new_number)

print("Data types")

# Int num
x = 14
print(x)
print(type(x))

# Float num
pi_num = 3.14
print(pi_num)
print(type(pi_num))

print("Conditions and Conditional Statements")


# defining a function that turn message base on the temperature
def evaluate_temp(temp):
    # initial message
    message = "Normal temperature"

    # if the temperature is greather than 38
    if temp > 38:
        message = "Hot"
    return message

# Using evaluate_temp function
print(evaluate_temp(39))

# if...else condition
def evaluate_temp_two(temp):
    if temp > 38:
        message = "fever!"
    else:
        message = "not fever"
    return message

# using evaluate_temp_two
print(evaluate_temp_two(80))

# elif shorter of else if
def evaluate_temp_three(temp):
    if temp > 30:
        message = "fever"
    elif temp == 30:
        message = "not fever"
    else:
        message = "oops"
    return message

#calling evaluate_temp_three

print(evaluate_temp_three(22))


# Creating simple list
flowers = ["red", "green", "yellow"]

print(type(flowers))
print(flowers)

# Length of the list
print(len(flowers))

# Slicing
# First two entries
print(flowers[:2])

# Last two entries
print(flowers[-2:])

# Adding item
flowers.append("black")

# Print the list
print(flowers)

# If condition
egg = 5
if egg > 0:
    print("egg is bigger than 0")

# Using Help function
help(print)

# Using lists

primeNumbers = [1, 2, 3, 4]

print(primeNumbers[0])

# Creating list in list

myList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing list inside list
print(myList[0][1])

# print the list primeNumbers
print(primeNumbers)

# Changing the value of primeNumber[0]

primeNumbers[0] = 'Hello :D'

# Print the new value of primeNumbers[0]

print(primeNumbers[0])

# Loops

for primes in primeNumbers:
    print(primes, end=' ')
