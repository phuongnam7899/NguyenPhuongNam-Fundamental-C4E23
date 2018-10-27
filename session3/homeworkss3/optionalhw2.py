from random import *
secret_word=["h","e","l","l","o"]
shuffled_word= sample(secret_word,len(secret_word))
print(*shuffled_word,sep=" | ")
guess_word=input("guess the word ")
while list(guess_word) != (secret_word):
    print("wrong")
    guess_word=input("guess the word")
print("good")