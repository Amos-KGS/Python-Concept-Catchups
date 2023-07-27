# Variable declarations
# /*-- Numbers --*/
# whole numbers

mywholeNum = int(8)
print(mywholeNum) # output(8)

# Floating numbers (With decimal places)
myFloatNum = float(8)
print(myFloatNum) # output(8.0)

# /*-- Strings--*/
# Often use single quotes or double quotes
myName =str("Your Name")
print(myName)

# /*-- Simulataneous Assignment of Variables --*/
a,b,c = 4,6,9
print(a,b,c)

# /* Test Code */

# Variables definitions
mystring = 'hello'
myfloat = float(10)
myint = int(20)

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)