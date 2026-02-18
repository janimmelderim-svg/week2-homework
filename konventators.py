#konstantes
KM_TO_MI=0.621371
KG_TO_LB=2.20462
L_TO_GAL=0.264172
USD_TO_EUR=0.8435
#galvenā izvēlne
print("Izvēlies konversiju")
print("1. km<-> mi")
print("2. kg<-> lb")
print("3. l<-> gal")
print("4. USD<-> EUR")
conversion_type=input(">")
#pārbaude vai izvēle ir derīga
if conversion_type not in ["1", "2", "3", "4"]:
    print("Nederīga izvēle. Lūdzu, izvēlieties ciparu no 1 līdz 4.")
    exit()
print("virziens:")
print("1. uz priekšu")
print("2. uz atpakaļ")
direction=input(">")
if direction not in ["1", "2"]:
    print("Nederīga izvēle. Lūdzu, izvēlieties ciparu no 1 līdz 2.")
    exit()
try:
    value=float(input("ievadi vērtību: "))
except ValueError:
    print("Kļūda. Lūdzu, ievadiet skaitli.")
    exit()
if conversion_type=="1":
    if direction=="1":
        result=value*KM_TO_MI
        print(f"{value:.2f} kilometri ir {result:.2f} jūdzes.")
    elif direction=="2":
        result=value/KM_TO_MI
        print(f"{value:.2f} jūdzes ir {result:.2f} kilometri.")
elif conversion_type=="2":
    if direction=="1":
        result=value*KG_TO_LB
        print(f"{value:.2f} kilogrami ir {result:.2f} mārciņas.")
    elif direction=="2":
        result=value/KG_TO_LB
        print(f"{value:.2f} mārciņas ir {result:.2f} kilogrami.")
elif conversion_type=="3":
    if direction=="1":
        result=value*L_TO_GAL
        print(f"{value:.2f} litri ir {result:.2f} galoni.")
    elif direction=="2":
        result=value/L_TO_GAL
        print(f"{value:.2f} galoni ir {result:.2f} litri.")
elif conversion_type=="4":
    if direction=="1":
        result=value*USD_TO_EUR
        print(f"{value:.2f} dolāri ir {result:.2f} eiro.")
    elif direction=="2":
        result=value/USD_TO_EUR
        print(f"{value:.2f} eiro ir {result:.2f} dolāri.")
