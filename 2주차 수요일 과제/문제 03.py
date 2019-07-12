matrix=list()
All=0
for i in range(0,9):
    matrix.append(int(input()))
    All +=matrix[i]


for i in range(0,9):
    for q in range(i,9):
        if (All-matrix[i]-matrix[q])==100:
            fir=i
            sec=q
            break

del matrix[sec], matrix[fir]
matrix.sort()

for i in range(len(matrix)):
    print(matrix[i])
