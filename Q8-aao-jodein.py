elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
while i<len(elements):
    if elements[i]%2==0:
       sum=sum+elements[i]
    else:
        sum1=sum1+elements[i]
    i+=1
print("sum of even number  =",sum)
print("sum of odd number =",sum1)





# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# sum1=0
# even=0
# odd=0
# while i<len(elements):
#     if elements[i]%2==0:
#         even+=1
#         sum=sum+elements[i]
#     else:
#         odd+=1
#         sum1=sum1+elements[i]
#     i+=1
# print("even =",sum)
# print("odd =",sum1)