import json
import random
import urllib.request

url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words = json.loads(url.read())
random_word = random.choice(words)
lrandom_word=list(random_word)
guess_word='*'*len(random_word)
lguess_word=list(guess_word)
final=''
print("WELCOME TO HANGMAN GAME!")
print("Ready to play.....")
n=int(input("Enter the number of incorrect attempt a player can guess:"))
while n>0:
    if final=='':
       print("guess word:",guess_word)
    else:
        print("guess word:",final)
    print("number of wrong attempt remaining:",n) 
    c=str(input("enter the guess character:")) 
    if c in lrandom_word:
        final=''
        for i in range(len(random_word)):
            if c==lrandom_word[i]:
                lguess_word[i]=c
                lrandom_word[i]=''
        
        for j in lguess_word:
            final+=j
        if final==random_word:
            print("\nWoW!!! Correct Answer is:",random_word)
            print("You win the game!!!")
            break
        n=n
    else:
        print("\nIncorrect guess:")
        n=n-1
    if n==0:
        print("\nSorry!!! Correct Answer is:",random_word)
        print("You lose the game!!!!\nTry Again!!!")
