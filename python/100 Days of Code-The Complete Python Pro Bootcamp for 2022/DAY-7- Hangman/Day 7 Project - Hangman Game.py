import random
import art
import words

def convert_list_to_string(a):
    blank_word = ' '
    for char in a:
        blank_word += char
    return( blank_word )
# choosing a word randomly.
word_chosen = random.choice( words.word_list )
blank_word = [ ]
lives = 6
end_of_game = False

for char in word_chosen:
    blank_word += '_'

print( word_chosen )
print(art.logo)
print( convert_list_to_string(blank_word) )

while not end_of_game: 
    i = 0
    guessed_word = input("\n\n Guess a word: ").lower()

    if guessed_word in blank_word:
        print(f" You have used {guessed_word} before.")
# check if the user guessed letter is one of the letters in the words_chosen
    for char in word_chosen:
        i += 1
        if guessed_word == char:
            blank_word[ i - 1 ] = char
            print( convert_list_to_string(blank_word)) 
            print(art.stages[lives])
# if the guessed word is not in word_chosen then reduce lives by 1.
    if guessed_word not in word_chosen:
        lives -= 1
        print(f" You guessed {guessed_word}, that's not in the word. You lose a life.")
        print( convert_list_to_string(blank_word)) 
        print(art.stages[lives])
        if lives == 0:
            end_of_game = True
            print(" You have lost the game.\n Better luck next time.")
# if there are no more '_' then end the game.    
    if '_' not in blank_word:
        end_of_game = True
        print(" Congratulation you have won the game.")