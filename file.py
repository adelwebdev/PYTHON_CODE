# print("word")
# num1 = input("enter the first number:  ")
# num2 = input("enter the second  number:  ")

# result = float(num1) + float(num2)
# print(result)

# color = input("enter a color: ")
# pluralNoun = input("enter a plural noun: " )
# celebrety = input("enter a celebrety: ")

# print ("roses are " + color)
# print (pluralNoun + "  are blue")
# print ("i love " + celebrety)

#----------------------------------------------- list---------------------------------------------------

friends =  [ "Kevin", "Adel", "Tom", "frank", "jimmy"]
friends[1] = "Mike"
print((friends))
# --------------on peut utiliser le négatif pour acceder au tableau en sens inverse-----------------
print(friends[1:3])

numbers = [2, 45, 454, 23, 7, 54]
print(numbers)
friends.extend(numbers)
friends.insert(1, "new name")
friends.remove("Tom")
friends.pop()
print(friends)
print(friends.index("frank"))







