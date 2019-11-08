names = ["Amelia", "Ava", "Brave", "Jessica","Isla", "Olivia", "Poppy", "Precious"]


found = False
def Linear_search(list_name, name_sought):
    global found
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

name = Linear_search(names, "Brave")
print(name)
