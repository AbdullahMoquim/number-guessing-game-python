import random

def main():
  play_again = "yes"
  while play_again == "yes":
    print("""
    Welcome to the Number Guessing Game!
        Game Features:
        1. Choose Easy, Medium, or Hard difficulty.
        2. Each level has a different number range and number of attempts.
        3. Get Too High / Too Low hints.
        4. Attempts are tracked.
        5. Performance shown after each round.
        6. Replay after the game ends.
    """)
    
    difficulty = input("Choose a difficulty (Easy, Medium, Hard): ").lower()
    if difficulty == "easy":
      secret_number = random.randint(1, 50)
      max_attempts = 10
    elif difficulty == "medium":
      secret_number = random.randint(1, 100)
      max_attempts = 8
    else:
      secret_number = random.randint(1, 200)
      max_attempts = 6
    
    attempts = 0 
    guess = int(input("Enter your guess: "))
    while guess != secret_number and attempts < max_attempts:
      attempts += 1
      if guess > secret_number:
        print ("Too high")
      elif guess < secret_number:
        print("Too low")

      guess = int(input("Enter your guess: "))

    attempts += 1
    if guess == secret_number:
      print("Correct!")
      print(f"Number of attempts:{attempts}")
    else:
      print("You ran out of attempts!")
      print(f"The correct number was:{secret_number}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
  print("Thanks for playing!")
    













if __name__ == "__main__":
  main()