nbList = []

nbDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8, 
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50, 
    "sixty": 60,
    "seventy": 70, 
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000
}

strNB = input("Enter the number you want to convert: ").lower()
strNB += " "

y = ""
for x in strNB:
    y = y + x
    
    if x == " ":
        y = y.removesuffix(" ")
        nbList.append(y)
        y = ""
        
while "" in nbList:
    nbList.pop(nbList.index(""))

total = 0
valeur_cumulee = 0

for x in nbList:
    valeur_act = nbDict[x]
    
    if valeur_act == 100:
        valeur_cumulee *= valeur_act
        
    elif valeur_act == 1000:
        valeur_cumulee *= valeur_act
        total += valeur_cumulee
        valeur_cumulee = 0
        
    else:
        valeur_cumulee += valeur_act

total += valeur_cumulee

print(total)