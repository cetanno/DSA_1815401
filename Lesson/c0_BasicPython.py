#This is how you comment in Python.
print("Output") #OUTPUT SYNTAX

a = 12345 #INITIALIZATION
b = 54321
print(a,b,"yes") #MULTIPLE OUTPUTS SYNTAX

a,b,q = b,a,"cie" #SWAP AND ASSIGNING MULTIPLE VALUES
print(a,b,q)

print("Input string here")
c = input() #INPUT, THIS FUNCTION ASSUMES THE INPUT TO BE A STRING
print("and number here")
cnum = float(input()) #INTEGER INPUT float(),int()
print(c, "is the input while", cnum, "is the integer input")

#DATA TYPES
yes = True
no = False
name = "DATA STRUCTURE AND ALGORITHM"
print(yes, no, name)

#IF ELIF AND ELSE STATEMENTS
if(a > b):
    print("a is larger than b")
    print("yes")
elif(a < b): #EQUIVALENT TO ELSE IF
    print("b is larger than a")
else:
    print("a and b are equal")

#OPERATORS
print("Operators")
print(13+2, "Addition")
print(13-2, "Subtraction")
print(13*2, "Multiplication")
print(13/2, "Division")
print(13%2, "Modulus")
print(13**2, "Exponentiation")
print(13//2, "Floor Division")

#FOR LOOP
for i in range(3): #DEFAULT INITIAL 0 if 1 parameter
    print("Loop A is repeated", i+1, "times.")

for i in range(6,10): #6,7,8,9. it does not hit 10
    print("Loop B is repeated", i, "times.")

for i in "PYTHON": #Looping a string
    print("The letter is", i)

arr = [12,51,85,19,28]
for i in arr: #Looping an array
    print(i)

#WHILE LOOP
total = 0
i = 1 #Initialize
while(i<10): #The checking
    total += i
    i += 1 #The update
print("Total for this Loop C is",total)

#FUNCTION
def Add2Number(a,b=1):
    return a + b

def sayHello():
    print("Hello World")

print(Add2Number(10,5))
print(Add2Number(10))
# print(Add2Number())  THIS WILL RETURN AN ERROR
sayHello()

#COMPARATORS
yes = True
no = False

print("AND")
print(yes and yes)
print(yes and no)
print(no and yes)
print(no and no)

print("OR")
print(yes or yes)
print(yes or no)
print(no or yes)
print(no or no)

print("NOT")
print(not yes)
print(not no)