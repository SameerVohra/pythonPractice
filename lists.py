dogs = ["Roger", 1, "Sid", True, "Quincky", 7]
print(dogs[3]) #Will print the item at index 3

print(dogs[2:4]) #Wil print the items from index 2 to 3

dogs[2] = "Bob" #Will update the value of index 2 to 'Bob'

print(dogs[3:]) #Wll start from index 3 and goes till the end

print(dogs[:4]) #Will start form starting and will go till index 4

print(dogs[:]) #Will return the whole list from start to end

print(len(dogs)) #will return the length of the list

dogs.append(106)
print(dogs)

dogs.extend(['Lily', 'Charlie'])
print(dogs)

dogs.remove(106)
print(dogs)

dogs.pop()
print(dogs)

dogs.insert(2, "Max")
print(dogs)

items = [1,3,6,2,8,22,1,0]
items.sort()
print(items)

copy_dogs = dogs[:]
print(copy_dogs)
