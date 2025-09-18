word = input()
new_word = ""
for i in word:
    if i.islower():
        new_word += i.upper()
    elif i.isupper():
        new_word += i.lower()
    else :
        new_word += i
print(new_word)