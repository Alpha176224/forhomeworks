#   a=eval(input())
# b=eval(input())
# myset=set(a).symmetric_difference(set(b))
# mylist=list()
# for i in set(myset):
#     n=a.count(i)+b.count(i)
#     for j in range(1,n+1):
#         mylist.append(i)
# print(mylist)

# n=int(input())
# for i in range(1, n):
#     print(i**2)

# import random
# def play_game(): 
#     number = random.randint(1, 100)
#     attempts = 10

#     while attempts > 0:
#         try:
           
#             guess = int(input(f"You have {attempts} attempts left. Enter your guess (1-100): "))
#         except ValueError:
#             print("Please enter a valid number.")
#             continue

        
#         if guess > number:
#             print("Too high!")
#         elif guess < number:
#             print("Too low!")
#         else:
#             print("You guessed it right!")
#             break
        
#         attempts -= 1

#     if attempts == 0:
#         print(f"You lost. The correct number was {number}. Want to play again?")

# def main():
#     while True:
#         play_game()
        
       
#         play_again = input("Enter 'Y', 'YES', 'y', 'yes', or 'ok' to play again: ").strip().lower()
#         if play_again not in ['y', 'yes', 'ok']:
#             print("Thanks for playing!")
#             break



# password = input("Enter a password: ")
# if len(password) < 8:
#     print("Password is too short.")
# elif not any(char.isupper() for char in password):
#     print("Password must contain an uppercase letter.")
# else:
#     print("Password is strong.")


# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# for number in range(1, 101):
#     if is_prime(number):
#         print(number)