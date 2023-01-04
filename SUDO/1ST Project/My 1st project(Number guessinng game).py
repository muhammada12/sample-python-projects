x = int(input())
y = int(input())

def calculation():
    if x > y and x != 0:
        i = (x + (y - x)) * y
        i = i + x
        if i % 2 == 0:
            value = (i // y) + x

        else:
            value = (i // x) + y - 1

    elif y > x and y != 0:
        j = x * (y + x + (y + 1))
        j = j + y
        if j % 2 == 0:
            value = (j // x) + y + 4

        else:
            value = (j // y) + x - 2

    def game_guess():
        secret_number = value
        secret = ""
        guess_count = 0
        input_chances = int(input("How many times? "))
        out_of_chances = False
        while secret != secret_number and not (out_of_chances):
            if guess_count < input_chances:
                secret = int(input("Enter your hope! "))
                guess_count = guess_count + 1
            else:
               out_of_chances = True
        if out_of_chances:
             print("You lose! Fuck you!")
        else:
             print("You win! Fuck you!")
    game_guess()

calculation()
