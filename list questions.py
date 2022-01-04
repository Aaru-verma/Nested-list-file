list1 =[[ 94, 86, 88],[71, 98, 65],[95, 45, 78]]
i=0
sum=0
while i<len(list1):
    j=0
    while j<len(list1[i]):
        if j==0:
           sum=sum+list1[i][j]
        j=j+1
    i+=1
print(sum)   




a =[1, 2, 10,[4, 19, 20],7]
i=0
b=[]
while i<len(a):
    if type(a)==b:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i+=1
c=0
sum=0
while c<len(b):
    sum=sum+a[c]
    c+=1
print(sum)


    b=a[i]
    j=0
    while j<len(b[i]):
        if type(b) is a:
            sum+=b[i][j]
            j+=1
        else:
            sum+=b[i][j]
        i+=1
    print(sum)





num=[[1,2,3],[4,5,6],[7,8,9]]
i=0
s=0
s1=0
s2=0
while i < len(num):
    j = 0 
    while j < len(num[i]):
        if num[i][j]==0:
            s = s+num[i][j]
        j+=1
    i+=1
    print(s)




num=[[1,2,3],[4,5,6],[7,8,9]]
i=0
s=0
while i<len(num):
    j=0
    while j<len(num):
        b=num[i][j]+num[i][j]
        s=s+num[i][j]
        j+=1
    i+=1
    print(s)





a=["aaru"]
print(a)

a=["string",12,True]
i=0
while i<=len(a):
    temp=type(a[i])
    print(temp)
    i=i+1
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))

a=list(input("enter the items:-"))
i=0
while i<len(a):
    if type(a[i])==type(a):
        print(type(a[i]))
    i+=1





a=[1,2,3,[4,5,6],2,3]
i=0
s=0
while i<len(a):
    if i==3:
        j=0
        sum=0
        while j<len(a[i]):
            sum+=a[i][j]
            j+=1
    else:
        s+=a[i]
    i+=1
print(sum+s)








Count unique values inside a list.
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
list=[]
i=0
while i < len(input_list):
    if input_list[i] not in list:
        list.append(input_list[i])
    i+=1
print(list)





numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
a=numbers[0]
b=0
while i<len(numbers):
    if numbers[i]>a:
        b=a
        a=numbers[i]
    elif numbers[i]>b and a!=numbers[i]:
        b=numbers[i]
    i+=1
print(b)


    



name=["poonam","tina","Aaru","pooja","Aachuki","Daksh"]
i=0
while i<len(name):
    if len(name[i])%2==0:
        print(len(name[i]),":-","even","=",name[i])
    else:
        print(len(name[i]),":-","odd","=",name[i])
    i+=1
# print((name[i]))





a=["Aaru",2.4,11,"2.8",3.9,56]
i=0
b=[]
while i<len(a):
    if type(a[i])==float:
        b.append(a[i])
    i+=1
print(b)
  




# name=input("enter the name:-")
# i=0
# while i<len(name):
#     if len(name[i])%2==0:
#         print(len(name[i]),"even")
#     else:
#         print(len(name[i]),"odd")
#     i+=1
# # # print(len(name[i]))








# a=[38,4,5,25,78]
# # count=0
# i=0
# while i<len(a):
#     # count=count+1
#     i=i+1
# print(i)




# list=[1,4,4,5,7,6,8,9,9,6,5,5,4,1,1,4]
# num=[]
# i=0
# a=0
# b=0
# c=0
# d=0
# e=0
# f=0
# g=0
# while i<len(list):
#     if list[i]==1:
#         a+=1 
#     elif list[i]==4:
#         b+=1
#     elif list[i]==5:
#         c+=1
#     elif list[i]==7:
#         d+=1
#     elif list[i]==6:
#         e+=1
#     elif list[i]==8:
#         f+=1
#     else:
#         g+=1
#     i+=1
# num.extend([[1,a],[4,b],[5,c],[7,d],[6,e],[8,f],[9,g]])
# print(num)






# num=list(input("enter the items:-"))
# num=[1,4,4,5,7,6,8,9,9,6,5,5,4,1,1,4]
# list=[]
# count=0
# i=0
# while i<len(num):
#     j=0
#     while j<len(num[i]):
#         if count==num[i][j]:
#             list.append(num[i][j])
#         j+=1
#         count+=i
#     i+=1
# print(num[i],count)

    





# num=list(input("enter your number:"))
# i=0
# c=0
# while i<len(num):
#     j=0
#     while j<len(num[i]):
#         if num[i]==num[i][j]:
#             j=j+1
#             c=c+i
#         i=i+1
# print(c)










# num=list(input("enter numbers:"))
# d=[]
# for i in num:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]=d[i]+1
# print(d)






# a=[1,4,7,8,3,6,17,20,12,15]
# a.sort()
# i=0
# while i<len(a):
#     i+=1
# print(a)






# line=input("enter the sentence :")
# a=line.split()
# i=0
# while i< len(a):
#     i+=1
# print(a)





# sentence=input("enter the sentence:")
# z=sentence.title()
# i=0
# while i<len(z):
#     i+=1
# print(z)

  




# a=[4,8,7,2,5]
# i=0
# while i <len(a):
#     i+=1
#     print(a[-i])
# j=0
# while j<len(a):
#     j+=1
#     print(a[-j],end=" ")






# a=[2,4,5,8,6,10]
# b=[1,3,7,9]   
# a.extend(b)
# a.sort()
# i=0
# while i<len(a):
#     i+=1
# print(a)






a=[2,4,5,8,6,10]
b=[1,3,7,9]   
# a.extend(b)
i=0
while i < len(a):
    if a[i] not in b:
        a.extend(b)
    i+=1
print(a)
    # j=0
#     while j <len(a)-i-1:
#         if a[j]>a[j+1]:
#             temp=a[j]
#             a[j]=a[j+1]
#             a[j+1]=temp
#         j+=1
#     i+=1
# print(a)





# a=[2,6,5,7,1,10]
# i=0
# while i<len(a):
#     i+=1
#     print(a[-i]) 
# j=0
# while j<len(a):
#     j+=1
#     print(a[-j],end=" ")
    
    
    
    
    
# a=[3,5,7,7,9,6,8]
# b=[]
# i=0
# while i < len(a):
#     c=a[i]
#     n=3
#     b.append(c)
#     b.append(n)
#     i+=1
# print(b)
