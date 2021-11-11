elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]

i=0
count = 0
count1 = 0
sum=0
sum1=0
avg=0
avg1=0
while i < len(elements):
    if elements[i]%2==0:
        count+=1
        sum = sum + elements[i]
        avg = sum / count
    else:
        count1+=1
        sum1 = sum1 + elements[i]
        avg1 = sum1 / count1
    i+=1
print("sum of even numbers :",sum,"\n","average of even numbers:",avg,"\n","count of even numbers:",count)
print("sum of odd numbers :",sum1,"\n","average of odd numbers:",avg1,"\n","count of odd numbers:",count1)
