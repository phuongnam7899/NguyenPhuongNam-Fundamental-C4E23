quiz={
    "if x=8,then what is the value of 4(x+3)?" : [35,36,40,44],
    "i am 20 year old now and my brother is 5,how many years later will my age double my brother one?" : [5,10,15,20],
    "i have 3 apples, when my mother come back from market,she bought me more 3 pineapple, how many pineapple would i have? " : [3,4,5,6],
    "A grandmother have 3 daughter, each of them have 2 sister,their father and husband died and they do not have children,how many people in that family?" : [10,7,4,12]
}
right_answer={"if x=8,then what is the value of 4(x+3)?": 4,
    "i am 20 year old now and my brother is 5,how many years later will my age double my brother one?" : 2,
    "i have 3 apples, when my mother come back from market,she bought me more 3 pineapple, how many pineapple would i have? " : 1,
    "A grandmother have 3 daughter, each of them have 2 sister,their father and husband died and they do not have children,how many people in that family?" : 3
}
count_right_answer=0
for question in quiz:
    print(question)
    for i in range(1,5):
        print(i,".",quiz[question][i-1])
    us_answer= int(input("your answer:"))
    if us_answer == right_answer[question]:
        print("good job!")
        count_right_answer += 1
    else:
        print("slap yourself,please!))")
print("your result:",count_right_answer,"of",len(quiz),)