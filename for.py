#for number in range(1,11):
   # print(number)

vowels=0
consonant=0
for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels=vowels+1
    elif letter==" ":
        pass
    else:
        consonant=consonant+1
print("There are {} vowels".format(vowels))
print("There are {} consonant".format(consonant))
