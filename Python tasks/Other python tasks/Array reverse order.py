total = 0
Numbers = [] 
for i in range(0, 5):
    num = input("Enter a number")
    Numbers.append(num)
    total += int(num)
    
average = total/6
print(Numbers[::-1])
print(total)
print(average)


