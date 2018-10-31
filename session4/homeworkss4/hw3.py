prices={
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":15,
}
stock={
    "banana":6,
    "apple":0,
    "orange":32,
    "pear":15,
}
for fruit in prices:
    print(fruit)
    print("- price:", prices[fruit],"$")
    print("- stock:", stock[fruit],)

total=0
for fruit in prices:
    money= prices[fruit]*stock[fruit]
    total += money
print("if i sold all of my food, iwill have",total,"$")