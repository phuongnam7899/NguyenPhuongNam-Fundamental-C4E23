from random import *
secret_words = [["h","e","l","l","o"],["b","y","e"],["t","e","s","t"],["h","e","r","o"],["t","e","c","h","k","i","d"]]
while True:
    i=randint(1,len(secret_words)-1)
    secret_word= secret_words[i]
    shuffled_word= sample(secret_word,len(secret_word))
    print(*(shuffled_word),sep=" | ")
    guess_word=input("guess the word ")
    count=1
    while list(guess_word) != (secret_word):
        print("wrong")
        guess_word=input("guess the word")
        count += 1
    print("good,you need ",count," times to guess" )
    