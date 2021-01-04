alko = input("Podaj wynik w promilach: ")

if float(alko) == 0:
    print("Gratulacje jesteś trzeźwy!")
elif float(alko) > 0 and float(alko) <= 0.2:
    print("Możesz jechać ale musisz uważać")
elif float(alko) > 0.2 and float(alko) < 0.5:
    print("Oj będzie mandacik")
elif float(alko) >= 0.5:
    print("Prawo jazdy i dowód rejestracyjny")