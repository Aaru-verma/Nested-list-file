# a=[1,4,7,8,3,46,67,78]
# i=0
# while i < len(a):
#     j=0
#     while j <len(a)-i-1:
#         if a[j]>a[j+1]:
#             temp=a[j]
#             a[j]=a[j+1]
#             a[j+1]=temp
#         j+=1
#     i+=1
# print(a)



a=[1,4,7,8,3,6,17,20,12,15]
i=0
while i < len(a):
    j=0
    while j <len(a)-i-1:
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
        j+=1
    i+=1
print(a)

