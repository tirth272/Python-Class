#1
x = input('Enter value of x: ')
y = input('Enter value of y: ')


temp = x
x = y
y = temp

print("The value of x after swapping: ",x)
print("The value of y after swapping: ",y)

#2
a = 5
b = 10

a, b = b, a
print("a =", a)
print("b =", b)
