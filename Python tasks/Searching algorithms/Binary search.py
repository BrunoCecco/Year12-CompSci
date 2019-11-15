names = ["Amelia", "Ava", "Brave", "Jessica","Isla", "Olivia", "Poppy", "Precious"]


name_sought = input("Enter a name to be found")
found = False
def Binary_search(list_name, name_sought):
    global found
    index = -1
    midpoint = 0
    first = 0
    last = len(list_name)-1
    while found == False:
        for index in range(len(list_name)):
            midpoint = (first+last)//2
            if list_name[midpoint] == name_sought:
                name_index = midpoint
                found = True
            else:
                if list_name[midpoint] < name_sought:
                    first = midpoint + 1
                else:
                    last = midpoint - 1
                #endif
            #endif
        #next
    #endwhile
    return name_index
#endfunction

name = Binary_search(names, name_sought)
print(name)
