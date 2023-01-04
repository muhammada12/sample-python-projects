x = int(input("Let's Feed 'x' to the Engine:"))
y = int(input("Let's Feed 'y' to the Engine:"))
print(
    "Let's guess, \nWhich number would be produced by this Engine!\nSee you next line! \n\nLet me check your intellectuality!\n")


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
    value1 = value - x
    value2 = value - y
    def game_guess():
        secret_number = value
        secret = ""
        guess_count = 0
        input_chances = int(input("\nHow many times(chances)? Input: "))
        out_of_chances = False
        while secret != secret_number and not (out_of_chances):
            if guess_count < input_chances:
                secret = int(input("Enter your hope! Input: "))
                if secret > value:
                    print("Wrong Answer! Number is greater than to Secret!\n")
                elif secret < value:
                    print("Wrong Answer! Number is smaller than to Secret!\n")
                guess_count += 1
            else:
                out_of_chances = True

        if out_of_chances:
            print("You lose!")
        else:
            print("You win!")
        print("Output produced by this Engine: ", value, "\n" + "Let's try again,With some different values.")
    hints = str(input("Wanna get some hints?\nPress upper case 'YES' or 'NO':"))
    if hints == "YES":
        print("Hints are running through substrack with secret combination of x and y for x, y\nAlso you'll get some informations after wrong submition")
        print("substrack values for secret - x:", value1)
        print("substrack values for secret - y:", value2)
    else:
        print("Brave!")

    game_guess()
calculation()