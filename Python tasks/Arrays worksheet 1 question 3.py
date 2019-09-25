Outlets =[]

Outlet1 = [10, 12, 15, 10]
Outlet2 = [5, 8, 3, 6]
Outlet3 = [10, 12, 15, 10]
Outlets.append(Outlet1)
Outlets.append(Outlet2)
Outlets.append(Outlet3)
total = 0 
for i in range(0, 3):
    for j in range(0, 4):
        total = total + Outlets[i][j]
    print(total)
    total = 0

        
        
