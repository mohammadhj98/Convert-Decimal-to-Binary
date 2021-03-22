#mohammad haje forosh
#Conver Decimal number to Binary number!

print("Conver Decimal number to Binary number!")

number = int(input("Enter a number : "))
result = ""

while number != 0:
    remainder = number % 2  
    number = number // 2
    result = str(remainder) + result
print("The binary representation is", result)
