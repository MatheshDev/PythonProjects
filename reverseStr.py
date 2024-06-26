#convert the string into list of words
def strList(userStr : str):
    LtrList = []
    for l in userStr:
        LtrList.append(l)
    return LtrList

def revStr(newString):
    return newString[::-1]

newString = strList(str(input("Enter a text to reverse : ")))
print(revStr(newString))
        
#Damn!! Im really getting it!!