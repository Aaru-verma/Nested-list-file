question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?",    # teesra question
    "How many colors in rainbow?",
    "What is a manchester of India?"
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
    #fourth question ke liye options
    ["eight","seven","four","nine"],
    #fifth question ke liye options
    ["Gujarat","Rajasthan","delhi","Ahmedabad"]
]

# # har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1, 2, 4]
lifeline=[
    ["(1)Four" ,"(3)Seven"],
    ["(4)Delhi" ,"(2)Chennai"],
    ["(2)Counceling","(1)Software Engineerung"],
    ["(3)four" , "(2)seven"],
    ["(1)Gujrat" , "(4)Ahmedabad"]
]

print("Welcome to KBC  πΊπΊ π π")
i=0
money=0
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
        k=options_list[i][j]
        print(j+1,k)
        j+=1
    if count<2:
        n1=input("Do you want Lifeline?")
        if n1=="yes":
            count+=1
            print("50-50", lifeline[i])
    else:
            print("Sorryπ! You already used Lifeline")
    n2=int(input("Enter the answer:-"))
    if n2==solution_list[i]:
        money+=10000
        print("Your answer is correctππ")
        print("You winπ₯³ππ Rs./",money,"π΅π΅")
    else:
        print("Your answer is wrongππ")
        print("You can play againππ")
        print("You winπ₯³ππ Rs/",money,"π΅π΅")
        break
    i+=1
