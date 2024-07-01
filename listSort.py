num = [6,8,2,4,9]

def sortList(num):
    for i in range(0,len(num)-1):
        for j in range(i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    return num

print(sortList(num))