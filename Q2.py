marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
# Sum of the nested list given above - 1142.
i=0
s=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        s=s+marks[i][j]
        j+=1
    i+=1
print(s)






marks2 = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]
# Sum of the nested list given above - 965.
i = 0 
s = 0
while i < len(marks2):
    j = 0 
    while j < len(marks2[i]):
        s = s + marks2[i][j]
        j+=1
    i+=1
print(s)





marks3 = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
# Sum of the nested list given above - 1324.

i=0
sum=0
while i<len(marks3):
    j=0
    while j<len(marks3[i]):
        sum=sum+marks3[i][j]
        j+=1
    i+=1
    print(sum)
