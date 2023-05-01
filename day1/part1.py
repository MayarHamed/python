# 1
# fname=input('enter your first name:')
# lname=input('enter your last name:')
# print(f"Hey! {fname} {lname}")

# 2
# n=input('input any one digit integer: ')
# n1=int(n)
# n2=int(n+''+n)
# n3=int(n+''+n+''+n)
# print(n1+n2+n3)

# 3
# string="""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example"""
# print(string)

# 4
# import math

# radius = 6
# volume = (4/3) * math.pi * radius**3
# print(f"The volume of a sphere with radius {radius} is {volume:.2f}")

# 5
# base=int(input('enter triangle base: '))
# height=int(input('enter triangle height: '))
# area=(1/2)*base*height
# print(f"the area of the triangle with the given base and height is {area:.2f}")

# 6
# n = 5
# for i in range(n):  # first half
#     for j in range(i+1):
#         print("*", end=" ") #end function to write on the same line
#     print()
# for i in range(n-1):  # second half
#     for j in range(n-i-1):
#         print("*", end=" ")
#     print()

#7
# word = str(input('please enter one word: '))
# print(word[-1::-1])

#8 
# numbers = list(range(7))
# filtered_numbers = numbers[:3] + numbers[4:6]
# print(filtered_numbers)

#9
# a, b = 0, 1
# print(a,end="")
# print(b,end="")
# while b <= 50:
#     a, b = b, a + b
#     print(b, end="")

#10
string = input("Enter a string: ")
digits = 0
letters = 0
for char in string:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
print("Number of digits:", digits)
print("Number of letters:", letters)