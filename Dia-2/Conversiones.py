# Conversiones en Python

# Implicitas
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

print()

# Explicitas
num1 = 5.8

print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
edad = int(edad)

print(edad)
print(type(edad))

new_age = 1 + edad
print(type(new_age))
print(new_age)

print("Tu nueva edad va a ser " + str(new_age))