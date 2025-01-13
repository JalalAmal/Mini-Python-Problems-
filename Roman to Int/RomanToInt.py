"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
    """

def RomToInt(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    valeur_pre = 0
    for x in reversed(s):
        valeur_act = roman_values[x]
        if valeur_pre > valeur_act:
            total -= valeur_act
        else:
            total += valeur_act
        
        valeur_pre = valeur_act 
    return total

rom = input("Entrer un nb roman: ").upper()
print(RomToInt(rom))