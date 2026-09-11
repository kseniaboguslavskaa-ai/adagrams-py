from random import randint

def draw_letters():
    #Store how many times each letter appears
    how_many_letters = {
        'A': 9, 
         'B': 2, 
        'C': 2, 
        'D': 4, 
        'E': 12, 
        'F': 2, 
        'G': 3, 
        'H': 2, 
        'I': 9, 
        'J': 1, 
        'K': 1, 
        'L': 4, 
        'M': 2, 
        'N': 6, 
        'O': 8, 
        'P': 2, 
        'Q': 1, 
        'R': 6, 
        'S': 4, 
        'T': 6, 
        'U': 4, 
        'V': 2, 
        'W': 2, 
        'X': 1, 
        'Y': 2, 
        'Z': 1
    }
    #Create an empty pool for all letters
    letter_pool = []

    #Go throwgh each letter
    for letter in how_many_letters:

        #Get how many times this letter should appear
        amount = how_many_letters[letter]

        #Add the letter to the pool the correct number of times
        for i in range(amount):
            letter_pool.append(letter)

    #Create an empty hand 
    letter_bank = []

    #Repeat 10 times to get 10 letters
    for i in range(10):

        #Find hom many letters are left in the pool
        pool_length = len(letter_pool)

        #The last index in the pool is one less than the length
        last_index = pool_length - 1

        #Chose a random index in the pool
        random_index = randint(0, last_index)

        #Take the letter and remove it from the pool
        letter = letter_pool.pop(random_index)

        #Add the letter to player's hand
        letter_bank.append(letter)

    #Return 10 letters to the player
    return letter_bank

def uses_available_letters(word, letter_bank):
    #Make an empty copy of the hand
    letter_copy = []

    #Add all letters from the original hand to the copy
    for letter in letter_bank:
        letter_copy.append(letter)

    #Make the word uppercase so it matches the hand
    word = word.upper()

    #Go through each letter in the word
    for letter in word:

        #If the letter is available, use it once
        if letter in letter_copy:
            letter_copy.remove(letter)

        #If the letter is missing, we can not make the word
        else:
            return False
        
    #If all letters were found, we can make the word
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass