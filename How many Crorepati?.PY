kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count=0
count1=0
count2=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        count+=1
    elif kitna_paisa_hai[i]>=100000 and kitna_paisa_hai[i]<10000000:
        count1+=1
    else:
        count2+=1
    i+=1
print("Crorepati:-",count)
print("Lakhpati :-",count1)
print("Dilwale  :-",count2)





kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
crorepati=0
lakhpati=0
dilwale=0
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        crorepati+=1
        # print("Crorepati=",kitna_paisa_hai[i])
    elif kitna_paisa_hai[i]>=100000 and kitna_paisa_hai[i]<10000000:
        lakhpati+=1
        # print("Lakhpati=",kitna_paisa_hai[i])
    else:
        dilwale+=1
        # print("Dilwale=",kitna_paisa_hai[i])
    i+=1
print(crorepati,"crorepati")
print(lakhpati,"lakhpati")
print(dilwale,"dilwale")






