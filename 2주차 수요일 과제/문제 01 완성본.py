a1=['hawaii','happy']
lengthL=len(a1[0])
for i in range(1,len(a1)):
    if len(a1[i])<len(a1[i-1]):
        lengthL=len(a1[i])


numL=[]
for i in range(1,len(a1)):
    num=0
    for q in range(lengthL):
        if a1[i-1][q]==a1[i][q]:
            num +=1
            if q+1==lengthL:
                numL.append(num)
        else:
            numL.append(num)
            break;
            
numL.sort()
print(numL[0])
for i in range(numL[0]):
    print(a1[0][i],end='')
    
