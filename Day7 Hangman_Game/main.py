import random

from hangman_module import word_list
from hangman_art import stages 

lives =  6
# print(logo)
chosen_word = random.choice(word_list)
# print(chosen_word)
placeholder = ""
for position in range(len(chosen_word)):
  placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
  print(f"************************{lives}/6 LIVES LEFT ************************")
  guess = input("Guess a letter: ").lower()

  if guess in correct_letter:
    print(f"You have already guessed {guess}")
  
  display = ""
  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_letter.append(letter)
    elif letter in correct_letter:
      display += letter
    else:
      display += "_"
  
  print("Word to Guess :" + display)
  if guess is not chosen_word:
    lives -= 1
    print(f"You gussed {guess}, that's not in the word. You lose a life.")
    
    if lives == 0:
      game_over = True
      print(f"******** It was {chosen_word}You lose********")
  
  if "_" not in display:
    game_over = True
    print("********You win********")

  print(stages[lives])