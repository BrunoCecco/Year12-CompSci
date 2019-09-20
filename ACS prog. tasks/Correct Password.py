Password = "Tues1212"
String = str(input("Enter the correct password"))
for i in range(0, 3):
    if String == Password:
        print("Password accepted")
        break
    else: 
        print("Password rejected")
        String = str(input("Enter the correct password"))
	
