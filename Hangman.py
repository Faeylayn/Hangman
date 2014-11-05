import os
import random
import string

def get_words_list():
    words = ['black', 'white']
    return words

def get_word(word_list):
    index = random.randint(0, (len(word_list)-1))
    return word_list[index]

def make_word(word):
    l1 = []
    for s in word:
        l1.append(s)
    return l1

def make_guess(unguessed):
    guess = ""
    while guess not in unguessed:
        print "Please guess a letter."
        guess = raw_input()
        guess = string.lower(guess)
        if guess not in unguessed:
             print "That is an invalid guess"
    return guess        

def check_guess(word, guess):
    for i in range(len(word)):
        if word[i] == guess:
            return True
    return False

def replace_letter(guess, to_guess, word):
    index = []
    for i in range(len(word)):
        if word[i] == guess:
            index.append(i)
    for c in index:
        to_guess[c] = guess
    return to_guess

def make_unguessed():
    test = string.lowercase
    g = []
    for x in test:
        g.append(x)
    return g

def make_toguess(word):
    to_guess = []
    for x in word:
        to_guess.append("_")
    return to_guess

def remove_from_unguessed(guess, unguessed):
    l1 = []
    for x in unguessed:
        if x != guess:
            l1.append(x)
    return l1

def win_check(to_guess):
    for x in to_guess:
        if x == "_":
            return False
    return True

def another():
    "Ask the player if they would like to play another game."
    answer = ''
    while not (answer == 'Y' or answer == 'N'):
        print 'Would you like to play another game? (Y/N)'
        answer = raw_input()
       
    if answer == 'Y':
        print 'OK! Game On!'
        return True
    else:
        print 'OK! Goodbye!'
        return False

def main():
    while True:
        word_list = get_words_list()
        s_word = get_word(word_list)
        word = make_word(s_word)

        unguessed = make_unguessed()
        to_guess = make_toguess(word)
        guess_count = 7    
        guessed = []
        game_on = True
        while game_on:
            print to_guess
            print "Wrong guesses left: " + str(guess_count)
            print "Letters guessed:" 
            print guessed        
            guess = make_guess(unguessed)
    
            guessed.append(guess)
            unguessed = remove_from_unguessed(guess, unguessed)
            if check_guess(word, guess):
                to_guess = replace_letter(guess, to_guess, word)
                if win_check(to_guess):
                    print to_guess
                    print "You win!"
                    game_on = False
            else:
                guess_count -= 1
                if guess_count == 0:
                    print "You Lose!"
                    game_on = False

        if another() == False:
            break    


if __name__ == "__main__":

    main()
