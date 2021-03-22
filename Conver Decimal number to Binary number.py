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
#-----------------------------------------
# N=int(input("Enter a positive number in base 10: "))
# while(N<0):
#     N=int(input("Enter a positive number in base 10: "))
# #------------------------------------
# print("ravesh 1: Binary is: "+str(bin(N))[2:])
# #-----------------or-----------------
# r=''
# while(N>1):
#     r=r+str(N%2)
#     N=N//2
# r=r+str(N)
# print("ravesh 2: Binary is: "+r[::-1])