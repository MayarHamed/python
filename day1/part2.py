import random

##1
# def remove_adjacent_duplicates(nums):
#     result = []
#     for num in nums:
#         if not result or num != result[-1]:
#             result.append(num)
#     return result

# nums = [1, 2, 3, 3, 4, 4, 4, 5, 5]
# result = remove_adjacent_duplicates(nums)
# print(result)  

##2
# def front_back(a, b):
#     a_split = (len(a) + 1)
#     b_split = (len(b) + 1) 

#     a_front = a[:a_split]
#     a_back = a[a_split:]
#     b_front = b[:b_split]
#     b_back = b[b_split:]

#     print(a_front + b_front + a_back + b_back) 

# front_back('abcd', 'efgh')

##3
# def are_all_numbers_unique(numbers):
#     return len(numbers) == len(set(numbers))

# numbers1 = [1, 5, 7, 9]
# print(are_all_numbers_unique(numbers1))  
# numbers2 = [2, 4, 5, 5, 7, 9]
# print(are_all_numbers_unique(numbers2))  

##4
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# my_list = [64, 34, 25, 12, 22, 11, 90]
# sorted_list = bubble_sort(my_list)
# print(sorted_list)  

##5
# def guessing_game():
#     answer = random.randint(1, 100)
#     attempts = 10
#     guessed_numbers = []
#     while attempts > 0:
#         guess = input(f"You have {attempts} tries left. Guess a number between 1 and 100: ")
#         try:
#             guess = int(guess)
#             if guess < 1 or guess > 100:
#                 print("Number is out of range (1-100). Try again.")
#                 continue
#             if guess in guessed_numbers:
#                 print("You already guessed this number. Try again.")
#                 continue
#         except ValueError:
#             print("Please enter a valid number between 1 and 100.")
#             continue
#         guessed_numbers.append(guess)
#         if guess == answer:
#             print("Congratulations! You guessed the correct number!")
#             play_again = input("Do you want to play again? (y/n): ")
#             if play_again.lower() == 'y':
#                 guessing_game()
#             else:
#                 print("Thanks for playing!")
#             break
#         elif guess > answer:
#             print("Your guess is too high. Try again.")
#         else:
#             print("Your guess is too low. Try again.")
#         attempts -= 1
#     else:
#         print("You have no tries left.")
#         play_again = input("Do you want to play again? (y/n): ")
#         if play_again.lower() == 'y':
#             guessing_game()
#         else:
#             print("Thanks for playing!")
# guessing_game()