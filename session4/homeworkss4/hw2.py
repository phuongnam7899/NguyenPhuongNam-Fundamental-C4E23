inventory = {
    "gold" : 500,
    "pouch":["flint","twine","gemstone"],
    "backpack":["xilophone","dagger","bedroll"]
}
inventory["pocket"]=['seashell',"strage berry","lint"]
inventory["backpack"].remove("dagger")
inventory["gold"] += 50
print(inventory)