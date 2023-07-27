# How to Initialize a list and add values
mylist = []
# /**-- adding values to the list using append --*/
mylist.append(1)
mylist.append(3)
mylist.append(4)

# print list based on the index position.

print("First index value is " , mylist[0])
print('Last index value is', mylist[2])

# Print all list values using a loop

# Looping lists
for i in mylist:
    print('values in the list are: ', i)


for x in range(len(mylist)):
    print(mylist[x])

y = 0
while y < len(mylist):
    print("My list has: ",mylist[y])
    y= y+1


# /* -- Test list example --*/

numbers = [1,2,3]
strings = ['hello','World']
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)



# Joining 2 lists

List1 = ["Ams","Bsa","Dsa"]
List2 = [7,4,6]

for x in List2:
    List1.append(List2)

print(List1)



