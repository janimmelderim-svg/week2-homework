import random
while True:
    random_number = random.randint(1, 100)
    attempts_count = 0
    correct_guess = False
    print("Jauna spēle sākas! Uzmini skaitli no 1 līdz 100.")
    while attempts_count < 10:
        attempt=input(f"mēģinājums {attempts_count+1}/10: ")
        try:
            user_guess = int(attempt)
            attempts_count += 1
        except ValueError:
            print("Kļūda. Lūdzu, ievadi derīgu skaitli.")
            continue
        if user_guess ==random_number:
            print(f"Apsveicu! Tu uzminēji skaitli {random_number} ar {attempts_count} mēģinājumiem!")
            correct_guess = True
            break
        elif user_guess < random_number:
            print("Pārāk zems! Mēģini vēlreiz.")
        else:
            print("Pārāk augsts! Mēģini vēlreiz.")
    if not correct_guess:
        print(f"Tu neuzminēji skaitli. Skaitlis bija {random_number}.")
    play_again = input("Vai vēlies spēlēt vēlreiz? (j/n): ").lower()
    if play_again != "j":
        print("Paldies par spēlēšanu! Uz redzēšanos!")
        break