import mlab
from quiz import Questions
from random import choice,shuffle


mlab.connect()


point = 0
easy = Questions.objects(Difficulty="easy")
medium = Questions.objects(Difficulty="medium")
hard = Questions.objects(Difficulty="hard")
answered = []

def ques_make(question):
    print("Category:",question.Category)
    print("Type:",question.Type)
    print("Question:",ques.Question)
    cor_answer = question.Correct_answer
    inc_answer = question.Incorrect_answer
    inc_answer.append(cor_answer)
    shuffle(inc_answer)
    return inc_answer,cor_answer

while True:
    dif=input("Choose difficulty(e=easy , m=medium, h=hard):")
    while not (dif == "e" or dif == "m" or dif == "h"):
        dif=input("Choose difficulty(e=easy , m=medium, h=hard):")
    if dif == "e":
        ques = choice(easy)
        q = ques_make(ques)[0]
        for i in range(len(q)):
            print(q[i])
    elif dif == "m":
        ques = choice(medium)
        q = ques_make(ques)[0]
        for i in range(len(q)):
            print(q[i])
    elif dif == "h":
        ques = choice(medium)
        q = ques_make(ques)[0]
        for i in range(len(q)):
            print(q[i])
    user_answer = input("Type your answer:")

    if user_answer == ques_make(ques)[1]:
        print("Excactly!")
        if dif == "e":
            point += 1
        if dif == "m":
            point += 2
        if dif == "h":
            point += 3
        print("Your point :",point)
    else:
        print("You lost, come back later")
        print("Your point:",point)
        break
        




            
                


