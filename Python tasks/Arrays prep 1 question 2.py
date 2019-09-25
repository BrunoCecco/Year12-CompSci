Pupil = [0, 19]
for n in range(0, 19):
    pupil_name = input("Enter a pupil's name")
    Pupil.append(pupil_name)

print("GROUP 1")
for i in range(1, 19, 2):
    print(Pupil[i])
print("GROUP 2")
for j in range(0, 18, 2):
    print(Pupil[j])
