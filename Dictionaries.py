dog = {
    "name" : "Roger",
    "age" : 4
}

print(dog["name"])

dog["age"] = 6

print(dog)

print(dog.get("age"))

print(dog.keys())
print(list(dog.keys()))

print(dog.values())

print(list(dog.keys()))

print(len(dog))

dog["color"] = "black"
print(dog)

new_dog = dog.copy()
print(new_dog)

del dog['name']
print(dog)

dog.pop('color')
print(dog)

dog.popitem()
print(dog)
