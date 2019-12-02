Name = []
num_pupils = int(input("How many pupils are in your class"))
for i in range(num_pupils):
    pupil = input("Add pupil: ")
    Name.append(pupil)
pupil_name = input("What's the name of your pupil?")
for j in range(num_pupils):
    if pupil_name in Name:
        print("Pupil's record number: ", (Name.index(pupil_name)+1))
    else:
        print("Pupil not found")
        break
    break
