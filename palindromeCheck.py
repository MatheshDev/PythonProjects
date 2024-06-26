#convert the string into list of words
def strList(userStr : str):
    LtrList = []
    for l in userStr:
        LtrList.append(l)
    return LtrList

def revStr(strList):
    revStrList = strList[::-1]
    return revStrList

def checkPal(strList, revStrList):
    if(strList == revStrList):
        return "The given string is a Palindrome"
    else:
        return "The Given string is not a Palindrome"

Alist = strList("malayalam")
Blist = revStr(Alist)
print(checkPal(Alist,Blist))
