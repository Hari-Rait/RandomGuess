import random

def RandomGuess():

    Guesses_lst = []

    print("Welcome to the Guessing Game!")

    #secret_number = random.randint(1, 100)

    print("Gib ein Guess ein")
    guesses = input(str("Dein guess: "))
    Guesses_lst.append(guesses)

    print("gib noch ein Guess ein:")
    guesses2 = input(str("Dein 2. Guess: "))
    Guesses_lst.append(guesses2)

    print("möchstes du noch ein Guess eintragen?")
    nocheinguess = input(str("Ja oder Nein: "))
    if nocheinguess == "Ja":
        guesses3 = input(str("Dein 3. Guess: "))
        Guesses_lst.append(guesses3)

    elif nocheinguess == "Nein":
        print("dein Guess ist:" )
        print(random.choice(Guesses_lst))
    else:
        print("Bitte gib den richtigen Wert ein. JA/Nein")


if __name__ == "__main__":
    RandomGuess()