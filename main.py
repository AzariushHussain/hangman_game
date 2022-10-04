import random
from words import words
import string
def get_valid_word(words):
    word=random.choice(words)
    while'-' in word or  ' ' in word:
        word =random.choice(words)
    return word.upper()
def hangman():
    word = get_valid_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    lives=6
    while len(word_letters)>0 and lives>0:
        print(f"You have {lives} lives left and letters you have guessed are:- ",' '.join(used_letters))
        word_list={letter if letter in used_letters else '-'for letter in words}
        print ("current words =", ' '.join(word_list))
        user_letter=input("enter a letter  :-")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("You got it correct,keep going.")
            else:
                lives=lives-1
                print("letter is not in word.  ")
        elif user_letter in used_letters:
            print("you have already used this leter.  ")
        else:
            print("invalid character,consider entering an alphabet.  ")
    if lives==0:
        print(f"You died , the word was {word} ")
    else:
        print(f"you guessed the word  {word}...!!!")

hangman()
