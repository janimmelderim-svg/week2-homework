#definiējam funkciju, kas pārbauda vai ievadītais vecums ir derīgs
def valid_age():
    while True:
        try:
            vecums = int(input("Lūdzu, ievadi savu vecumu: "))
            if vecums < 0:
                print("Vecums nevar būt negatīvs. Lūdzu, mēģini vēlreiz.")
            else:
                return vecums
        except ValueError:
            print("Nederīga ievade. Lūdzu, ievadi skaitli.")
#definējam funkciju, kas pārveido "j"/"n" atbildes par boolean vērtībām
def yes_no_to_bool(response):
    while True:
        response=input(response+" (j/n): ").strip().lower()
        if response == "j":
            return True
        elif response == "n":
            return False
        else:
            print("Nederīga ievade. Lūdzu, ievadi 'j' vai 'n'.")
#galvenā ievade
vecums=valid_age()
ir_autovadītāja_apliecība=yes_no_to_bool("Vai tev ir autovadītāja apliecība?")
ir_studenta_apliecība=yes_no_to_bool("Vai tev ir studenta apliecība?")
ir_veterāna_apliecība=yes_no_to_bool("Vai tev ir veterāna apliecība?")
#pārbaudes
var_balsot=vecums>=18
var_īrēt_auto=ir_autovadītāja_apliecība and vecums>=21
var_saņemt_senioru_atlaidi=vecums>=65 or ir_veterāna_apliecība
var_saņemt_studentu_atlaidi=ir_studenta_apliecība and vecums>=16 and vecums<=26
#rezultātu izvadīšana
print("\n---")
print(f"Vai tu vari balsot: {'Jā ✓' if var_balsot else 'Nē ✗'}")
print(f"Vai tu vari īrēt auto: {'Jā ✓' if var_īrēt_auto else 'Nē ✗'}")
print(f"Vai tu vari saņemt senioru vai veterānu atlaidi: {'Jā ✓' if var_saņemt_senioru_atlaidi else 'Nē ✗'}")
print(f"Vai tu vari saņemt studentu atlaidi: {'Jā ✓' if var_saņemt_studentu_atlaidi else 'Nē ✗'}")