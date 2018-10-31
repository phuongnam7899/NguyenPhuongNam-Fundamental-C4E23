# person1={
# "name":"duc",
# "place": "Phong",
# "age":3,
# }
# person2={
# "name":"h.duc",
# "place": "Hai Phong",
# "age":23,
# }
p_list=[
{
"name":"duc",
"place": "Phong",     # JASON
"age":3,
},
{
"name":"h.duc",
"place": "Hai Phong",
"age":23,
}
]


#print(p_list)
p=p_list[0]
print(p_list[0])
print(p["age"])

for p in p_list:
    print(p)



