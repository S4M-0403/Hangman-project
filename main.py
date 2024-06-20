import random 
#importing random library/framework

from ascii_art import logo
print(logo)


print("Welcome to Chemistry Hangman!!")
print("You have to decode the chemical element from all the elements of the perodic table and have a total of 6 lives. If you fail to do so, your man is hanged and you lost!.")

lives = 6
end_of_game = False

#genrating random word
from words import word_list
random_word = random.choice(word_list).lower()
word_length = len(random_word)
print(random_word)
display = []

#creating blanks
for _ in range(word_length):
    display+= "_"

while not end_of_game:
    guess = input("Enter a letter: ").lower()
    
    if guess in display:
        print(f"You have already guessed {guess} try another one.")
    
    for i in range(word_length):
        letter = random_word[i]
        if letter == guess:
            display[i] = letter;

    if guess not in random_word:
        print("You choose the wrong letter")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost!")
            print(f"The word was {random_word}")
            
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        print("You win")
        end_of_game = True
        
    from ascii_art import stages
    print(stages[lives])
     