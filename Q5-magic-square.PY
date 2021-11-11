magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j <len(magic_square):
        sum=sum+magic_square[i][j]
        j+=1
    i+=1
    print(sum)
k=0
while k<len(magic_square):
    n=0
    sum1=0
    while n <len(magic_square):
        sum1=sum1+magic_square[k][n]
        n+=1
    k+=1
    print(sum1,end=" ")
if sum==sum1:
    print(" it is a magic square ")
else:
    print(" it not a magic square")



