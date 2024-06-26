def make_str_list(string :str):
    strList = []
    for s in string:
        strList.append(s)
    return strList

strList = make_str_list("Hello")

def countVowel(strList):
    vowelList = []
    for s in strList:
        if(s in ['a','e','i','o','u']):
            vowelList.append(s)
    return len(vowelList)

print(countVowel(strList))

#AnotherMethod

def count_vowel(nstring):
    vowels = "aeiouAEIOU"
    count = 0
    for strs in nstring:
        if strs in vowels:
            count += 1
    return count

nstring = "aeiou"
print(count_vowel(nstring))