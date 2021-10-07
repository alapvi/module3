letters = "TRWAGMYFPDXBNJZSQVHLCKE"

while True:
    dni = input("Your DNI:")
    letter = dni[-1].upper()
    number = dni[:-1]
    if (len(dni) == 9 and number.isdigit()):
        number = int(dni[:-1])
        break
    else:
        print("Format Incorect")

mod = number%23
if letters[mod] == letter:
    print("Correct")
else:
    print("Incorrect!")

