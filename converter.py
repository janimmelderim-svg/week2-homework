#konstatntes uz 2.17 feb
KM_TO_MI=0.621371
KG_TO_LB=2.20462
L_TO_GAL=0.264172
USD_TO_EUR=0.8435
#funkcijas konversijai
def km_to_miles(km):
    return km*KM_TO_MI
def miles_to_km(miles):
    return miles/KM_TO_MI
def kg_to_lb(kg):
    return kg*KG_TO_LB 
def lb_to_kg(lb):
    return lb/KG_TO_LB 
def l_to_gal(l):
    return l*L_TO_GAL
def gal_to_l(gal):
    return gal/L_TO_GAL
def usd_to_eur(usd):
    return usd*USD_TO_EUR
def eur_to_usd(eur):
    return eur/USD_TO_EUR
def show_menu():
    print("1. Kilometri uz jūdzēm")
    print("2. Jūdzes uz kilometriem")
    print("3. Kilogrami uz mārciņām")
    print("4. Mārciņas uz kilogramiem")
    print("5. Litri uz galoniem")
    print("6. Galoni uz litriem")
    print("7. Dolāri uz eiro")
    print("8. Eiro uz dolāriem")
    print("9. Iziet")
Show_menu()
choice=input("Izvēlieties konversijas veidu (1-9): ")
Value=float(input("ievadi skaitli:"))
if choice=="1":
    print(f"{Value} kilometri ir {km_to_miles(Value)} jūdzes.")
elif choice=="2":
    print(f"{Value} jūdzes ir {miles_to_km(Value)} kilometri.")
elif choice=="3":
    print(f"{Value} kilogrami ir {kg_to_lb(Value)} mārciņas.") 
elif choice=="4":
    print(f"{Value} mārciņas ir {lb_to_kg(Value)} kilogrami.")
elif choice=="5":
    print(f"{Value} litri ir {l_to_gal(Value)} galoni.")
elif choice=="6":
    print(f"{Value} galoni ir {gal_to_l(Value)} litri.")
elif choice=="7":
    print(f"{Value} dolāri ir {usd_to_eur(Value)} eiro.")
elif choice=="8":
    print(f"{Value} eiro ir {eur_to_usd(Value)} dolāri.")
elif choice=="9":
    print("Iziet no programmas.")
else:
    print("Nederīga izvēle. Lūdzu, izvēlieties ciparu no 1 līdz 9.")
while True:
    Show_menu()
    choice=input("Izvēlieties konversijas veidu (1-9): ")
    if choice=="9":
        print("Iziet no programmas.")
        break
    Value=float(input("ievadi skaitli:"))
    if choice=="1":
        print(f"{Value} kilometri ir {km_to_miles(Value)} jūdzes.")
    elif choice=="2":
        print(f"{Value} jūdzes ir {miles_to_km(Value)} kilometri.")
    elif choice=="3":
        print(f"{Value} kilogrami ir {kg_to_lb(Value)} mārciņas.") 
    elif choice=="4":
        print(f"{Value} mārciņas ir {lb_to_kg(Value)} kilogrami.")
    elif choice=="5":
        print(f"{Value} litri ir {l_to_gal(Value)} galoni.")
    elif choice=="6":
        print(f"{Value} galoni ir {gal_to_l(Value)} litri.")
    elif choice=="7":
        print(f"{Value} dolāri ir {usd_to_eur(Value)} eiro.")
    elif choice=="8":
        print(f"{Value} eiro ir {eur_to_usd(Value)} dolāri.")
    else:
        print("Nederīga izvēle. Lūdzu, izvēlieties ciparu no 1 līdz 9.")
