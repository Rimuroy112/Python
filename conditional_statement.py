# conditional statement

# marks = 70

# if marks == 60:
#     print("You will get the certificate")
# elif marks == 70:
#     print("Job opportunity")
# else:
#     print("Enroll again")


my_input = int(input("Enter a number: "))

if my_input % 3 == 0 and my_input % 5 == 0:
    print("Fizzbuzz")
elif my_input % 5 ==0:
    print("Buzz")
elif my_input % 3 == 0:
    print("Fizz")
else:
    print("Not a fizzbuzz number")