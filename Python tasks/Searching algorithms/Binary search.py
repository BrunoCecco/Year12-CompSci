names = ["Amelia", "Ava", "Brave", "Jessica","Isla", "Olivia", "Poppy", "Precious"]


name_sought = input("Enter a name to be found")
found = False
def Binary_search(list_name, name_sought):
    global found
    midpoint = 0
    while found == False:
        for index in range(len(list_name)):
            if list_name[index] == name_sought:
                name_index = index
                found = True
            else:
                index += 1
            #endif
        #next
    #endwhile
    return name_index
#endfunction

name = Binary_search(names, name_sought)
print(name)
