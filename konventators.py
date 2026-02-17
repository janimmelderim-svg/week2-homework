KM_TO_MI=0.621371
def km_to_miles(km):
    return km*KM_TO_MI
km=float(input("ievadi kilometru skaitu: "))
print(f"{km} kilometri ir {km_to_miles(km)} jūdzes.")
