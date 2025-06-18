# List

students = ["suresh","ramesh","rakesh"]
students.append("ganesh")
students[1] = "karish"        # Mutable

print(students[1])
print(len(students))
print(students[1:3])          # list slicing


# String

string = "hello how are you ?"

print(string[6:17])           # string slicing


# Dictionary   >> key-value pair

rahim = { 'name' : 'rahim', 'age' : 28, 'salary' : 20000 }
rahim['age'] = 17                       # Mutable
rahim['Occupation'] = 'Coder'
print(rahim)


# Set

number = {1,2,3,4,5,6,2,5}

print(number)

# tuple

my_tuple = (1,2,3,4,5)        
# my_tuple[4] = 6              # immutable

print(my_tuple[2])