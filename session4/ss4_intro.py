# person = ["TPT","HN",'NEU',25,3,2000,False]
#-------------------------------------------
# peroson = {}
# print(peroson)
# print(type(peroson))
#--------------------------------------------
person = {
     "name": "H.Duc"#key-value
}
print(person)
#---------------------------------------------
# person={
#     "name":"h.duc",
#     "place": "Hai Phong",
#     "age":23,
# }
# print(person)
# person["friend_count"]=257 #Creat
# print(person)
#---------------------------------------------
key=""
print(person[key])
if key in person:
    print(person[key])
else:
    print("key not found")