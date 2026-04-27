import random

def main():
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
  elif difficulty == "medium":
    secret_number = random.randint(1, 100)
  else:
    secret_number = random.randint(1, 200)
  
  attempts = 0 
  guess = int(input("Enter your guess: "))
  while guess != secret_number:
    attempts += 1
    if guess > secret_number:
      print ("Too high")
    else:
      print ("Too low")

    guess = int(input("Enter your guess: "))

  attempts += 1
  print("Correct!")
  print(f"Number of attempts: {attempts}")
    













if __name__ == "__main__":
  main()