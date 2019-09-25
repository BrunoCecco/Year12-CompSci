school = ["AAAA", "BBBB", "CCCC", "DDDD"]
medal = [4, 7, 1, 3]

school_num = int(input("enter school number"))
while school_num != -1:
    medal[school_num] = medal[school_num] + 1
    school_num = int(input("enter school number"))

for i in range(len(school)):
    print("School number ", i)
    print("School name ", school[i])
    print("Number of medals ", medal[i])
