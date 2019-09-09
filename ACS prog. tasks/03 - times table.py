# validation number from 1 - 10
# 12 times table

Num = int(input("Input number from 1 to 10"))
    
while Num < 1 or Num > 10:
    Num = int(input("Input number from 1 to 10"))
#end while
if Num == 99:
    break
for x in range(1,13):
    print(Num*x)
#next
