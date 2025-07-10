a = int(input("Enter a number between 1 and 10: "))

match a : 
    case 1:
        print("You won a charger")
    case 3:
        print("you won $3")
    case 6:
        print("you won camera")
    case _:
        print("Better luck next time")