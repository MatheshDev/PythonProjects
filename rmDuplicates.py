#Remove Duplicates from a List

list = [1,1,1,1,1,1]

def rmDup(list):
    nList = []
    for i in list:
        if i not in nList:
            nList.append(i)
    return nList

print(rmDup(list))
