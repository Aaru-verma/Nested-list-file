char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
char_list1 = []
i=0
a1=0
b=0
c=0
d=0
e=0
f=0
while i<len(char_list):
    if char_list[i]=="a":
        a1+=1 
    elif char_list[i]=="n":
        b+=1
    elif char_list[i]=="t":
        c+=1
    elif char_list[i]=="x":
        d+=1
    elif char_list[i]=="u":
        e+=1
    else:
        f+=1
    i+=1
char_list1.extend([["a",a1],["n",b],["t",c],["x",d],["u",e],["g",f]])
print(char_list1)

print("a :",a1, "time")
print("n :",b,"time")
print("t :",c, "time")
print("x :",d,"time")
print("u :",e,"time")
print("g :",f,"time")

    