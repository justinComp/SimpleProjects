#HangMan

import random
# random number generator
randNum = random.uniform(0, 1)

#  gather the words in the text file into a list
wordlists = []
with open('wordlist.txt', 'r') as wordlist:
    for words in wordlist:
        wordlists.append(words)

#picking out the word
wordpickedIndex = round(len(wordlists)*randNum)

pickedWord = wordlists[wordpickedIndex]

print(pickedWord)

lives = 5
lengthofWord = len(pickedWord)
guessWord = []

for underscore in range(lengthofWord-1):
    guessWord.append('_')

print(guessWord)
rightLetter = False
while lives > 0:
    if '_' in guessWord:
        letter = input('Guess a letter! ')
        for i in range(lengthofWord):
            if letter == pickedWord[i]:
                guessWord[i] = letter
                rightLetter = True
            # else:
            #     print("you already guessed this letter")
   
        if rightLetter == True:
            print(guessWord)
            rightLetter = False
        else: 
            lives -= 1
            print('Incorrect Letter, Please Try Again')
            print('Lives remaining: ' + str(lives))
    
    else:
        print("You got the word! It was " + str(pickedWord))
        break
        
        

    
