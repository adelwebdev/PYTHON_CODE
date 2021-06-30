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

#----------------------------------------------------- list---------------------------------------------------

friends =  [ "Kevin", "Adel", "Tom", "frank", "jimmy"]
friends[1] = "Mike"
print((friends))
# -----------------on peut utiliser le négatif pour acceder au tableau en sens inverse-----------------
print(friends[1:3])

numbers = [2, 45, 454, 23, 7, 54]
print(numbers)
friends.extend(numbers)
friends.insert(1, "new name")
friends.remove("Tom")
friends.pop()
print(friends)
print(friends.index("frank"))

coordiantes = (3, 4)
# coordiantes[1] = 12
print(coordiantes)

# --------------------------------------Functions in Python -----------------------------------------
# def firstFunction(a, b): 
#     print(a, b)

# def cube(num):
#     print("code")
#     return num*num*num
  
# result = cube(5) 
# print(result)  

# ------------------------------------ IF STATEMENET ---------------------------------------------
is_male = False
is_tall = False

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not (is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but you're tall")    
else:
    print("you are not a male and you are not tall")

# def max_num (num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(34, 44, 123))       

# num1 = float(input ("enter first number: ")) 
# op = input ("enter an operator: ")
# num2 = float(input ("enter second number: "))

# if op == "+":
#     print (num1 + num2)
# elif op == "*":
#     print (num1 * num2)
# elif op == "-":
#     print (num1 - num2)
# elif op == "/":
#     print (num1 / num2)        
# else:
#     print ("This is not a valide operator")    

# monthConversion = {
#     "Jan" : "January",
#     "Feb" : "February",
#     "Mar" : "March",
# }
# print (monthConversion["Jan"])

i = 1
while i <= 10:
    print (i)
    i += 1
print ("done with loop")    

# secretWord = "giraffe"
# guess = ""
# guessCount = 0
# guessLimit = 3 
# outofguesses = False
# while guess != secretWord and not(outofguesses):
#     if guessCount < guessLimit:
#      guess = input("enter guess: ")
#      guessCount += 1
#     else:
#         outofguesses = True

# if   outofguesses:  
#     print("you lost") 
# else:
#  print("you win")

array = ["me", "tom", "jim"]
for friend in array: 
    print(friend)

for index in range(5):
    if index == 0:
        print("first iteration")
    else: print ('not first') 

# print(2**4)

def raise_to_power (base_num, pow_num):
    result = 1
    for index in range(pow_num):
     result = result * base_num
    return result

print(raise_to_power(3, 5))    

    # for index in range(3, 9):
    #     print(index)

# number_grid = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11],
#     [0],
# ]
# print (number_grid[0][2])

# for row in number_grid:
#    for col in row:
#        print(col)

def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
                translation = translation + letter
                return translation

print(translate(input("enter a phrase: ")))          

print("Comments are fun")

























