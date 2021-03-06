#Problem 1: List Sorting

gods = ["Notus", "Momus", "Nereus", "Glaucus", "Heracles", "Eurus", "Aether", "Phosphorous", "Zelus", "Tartarus"]

def sortList(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j][0] > list[j+1][0]:
                list[j], list[j+1] = list[j+1], list[j]
            #if the first letter of the strings are same, then jump to next letter
            if list[j][0] == list[j+1][0]:
                ind = 1
                while True:
                    ind = ind + 1
                    list[j], list[j+1] = list[j+1], list[j]
                    if (list[j][ind] != list[j+1][ind]):
                        break
    print list            
    return list


#Approach 2 - Using the built-in function
def sortList2(list):
    list.sort()
    print list
    return list

if __name__ == "__main__":
    sorted_list_1 = sortList(gods)
    sorted_list_2 = sortList2(gods)
