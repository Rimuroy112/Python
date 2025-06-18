# Loop : for and while

my_list = ['Apple','mango','guava','banana']

for fruits in my_list:
    print(fruits)
for index,fruits in enumerate(my_list):
    print(index,fruits)

for item in range(1,20,2):
    print(item)

# while

count = 0
while count < 5:
    print('Hello')
    count+=1