# Hangman

import random
import hangman_words
import hangman_art

stages = hangman_art.stages
word = random.choice(hangman_words.word_list)
display = []
has_player_won = False
lives = 6

print(hangman_art.logo)

for letter in word:
    display.append("_")

print(display)

while not has_player_won:
    guess = input("Guessa a letter").lower()

    for n in range(len(word)):
        if guess == word[n]:
            display[n] = guess
    if guess not in word:
        lives -= 1
        if lives == 0:
            print("You've lost")
            has_player_won = True
            # print(stages[lives])


    print(display)
    print(stages[lives])

    if "_" not in display:
        print("You've won!")
        has_player_won = True






# for letter in word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# for n in range(0, len(word)):
#     if word[n] == guess:
#         print("wow")
#     else:
#         print("Wrong")


