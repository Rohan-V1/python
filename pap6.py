class TooSmall(Exception):
    pass
class TooLarge(Exception):
    pass
num=10
while num==10:
    try:
        i=int(input("Enter a number:"))
        if i<num:
            raise TooSmall
        elif i>num:
            raise TooLarge
        break
    except TooSmall: 
        print("The Value is TOO Small,TRY AGAIN......!")
    except TooLarge:
        print("The Value is TOO Large,TRY AGAIN.......!")
print("Congrualations! You Guessed It Correctly.....!")