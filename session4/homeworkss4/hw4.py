quiz_answer={
    "if x=8,then what is the value of 4(x+3)":[35,36,40,44]
}
answer={
     "if x=8,then what is the value of 4(x+3)": 44 
}
for ques in quiz_answer:
    print(ques)
for i in range(1,5):
    print( i ,"." , quiz_answer["if x=8,then what is the value of 4(x+3)"][i-1])
user_answer=int(input("your choice:"))
if user_answer == answer["if x=8,then what is the value of 4(x+3)"]:
    print("correct!")
else:
    print("incorrect!")