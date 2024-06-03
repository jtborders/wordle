import random

wordsfile = open("words.txt")
wordslist = []
for line in wordsfile:
    wordslist.append(line.strip())
    
guessfile = open("guesses.txt")
guesslist = []
for line in guessfile:
    guesslist.append(line.strip())

randnum = random.randint(0,len(wordslist))

chosenword = wordslist[randnum]

green = '\x1b[32m'
yellow = '\x1b[33m'
red = '\x1b[31m'
white = '\x1b[0m'
clear = '\x1b[K'
prev = '\x1b[F'

print('Welcome to Word Guesser\n'+
      'How to play: Guess five letter words to uncover the answer\n'+
      green+'Green letters are correct\n'+
      yellow+'Yellow letters are in the incorrect position\n'+
      white+'White letters are incorrect')

guessed = False
for i in range(6):
    greencheck = False
    yellowcheck = False
    guessoutputlist = []
    guess = input(f"Enter guess {i+1}: ")
    
    while guess not in set(guesslist):
        guess = input(prev+"Guess a valid five letter word: "+clear)
    
    
    for letter1 in range(len(guess)):
        greencheck = False
        yellowcheck = False
        workingletter = guess[letter1]
        
        for letter2 in range(len(chosenword)):
            
            if workingletter == chosenword[letter2]:
                if letter1 == letter2:
                    greencheck = True
                else:
                    yellowcheck = True
        if greencheck == True:
            guessoutputlist.append(green+workingletter)
        elif yellowcheck == True:
            guessoutputlist.append(yellow+workingletter)
        else:
            guessoutputlist.append(white+workingletter)
    
    guessoutputlist.append(white)
    guessoutput=''.join(guessoutputlist)
    
    print(prev+guessoutput+clear)
    
    if guess == chosenword:
        guessed = True
        break
    
if guessed==True:
    print(green+'Well Done!'+white)
else:
    print(red+'The word was '+chosenword+'. Try Again'+white)
