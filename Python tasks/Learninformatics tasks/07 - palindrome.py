#palindrome
word = str(input("Enter a six letter word"))

num_characters = 0
for character in word:
    num_characters += 1
#next
    
while num_characters != 6:
    word = str(input("Enter a six letter word"))
    num_characters = 0
    for character in word:
        num_characters += 1
    #next
#endwhile

string_reverse = ""
for character in word:
    string_reverse = character + string_reverse
#next
print(string_reverse)
    

