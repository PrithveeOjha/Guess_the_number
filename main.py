import random
from art import logo
print(logo)
#introduction
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

won = False

# make a function for comparison
def compare(chosen_mumber, user_number):
  global won
  if chosen_mumber == user_number:
    won = True
    return f"You got it! The answer was {user_number}."
  elif chosen_mumber > user_number:
    return "Too low."
  elif chosen_mumber < user_number:
    return "Too high."
    
#Select a number between 1 and 100
chosen_mumber = random.randint(1,100)
print(f"Pssst, the correct answer is {chosen_mumber}")

# choose difficulty, easy - 10 attempts, hard - 5 attempts
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
  attempts = 10
else :
  attempts = 5

#take inputs and compare - if higher say "too high", if lower say "too low"
while attempts != 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  user_number = int(input("Make a guess: "))
  print("Guess again")
  print(compare(chosen_mumber, user_number))
  attempts -= 1
  if won:
    exit()
  elif attempts == 0 and not won:
    print("You've run out of guesses, you lose.")
    