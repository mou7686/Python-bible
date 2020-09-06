#get sentence from user
original=input("Please enter a sentence: ").strip().lower()
#split sentence into words
words=original.split()
#print(words)give us the splitted word by default
#loop through words and convert to pig latin
new_words=[]
for word in words:
    #print(word)
#if starts with vowel, just add "yay"
    if word[0] in "aeiou":
        new_word=word+"yay"
        new_words.append(new_word)
#print(new_words)        
    
#Otherwise,move the first consonant cluser to end,and add "ay"
    else:
        vowel_pos=0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos=vowel_pos+1
            else:
                break
        cons=word[:vowel_pos]
        the_rest=word[vowel_pos:]
        new_word=the_rest+cons+"ay"
        new_words.append(new_word)
#stick words back together
    #put blank space and then use a joint method
output=" ".join(new_words)         
#output the final string
print(output)
