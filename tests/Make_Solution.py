'''
The user has to enter a number between 0 and 23
If the number is less than 8 display a message saying "too early to get up"
If the number is less than 12 display a message saying "Good morning"
If the number is less than 14 display a message saying "Lunch time!"
If the number is less than 18 display a message saying "Good afternoon"
If the number is equal to 18 display a message saying "Tea Time"
If the number is less than 19 display a message saying "Good evening"
If the number is less than 22 display a message saying "Nearly bedtime"
If the number is 23 display a message saying "Good night!"
Any other number is met with the response “Sorry, I don’t recognize that”
'''
number = -1

def main():
    global number
    number = int(input("Enter a number between 0 and 23: "))

    if number < 0 or number > 23:
        print("Sorry, I don’t recognize that")
    elif number < 8:
        print("Too early to get up")
    elif number < 12:
        print("Good morning")
    elif number < 14:
        print("Lunch time!")
    elif number < 18:
        print("Good afternoon")
    elif number == 18:
        print("Tea Time")
    elif number < 19:
        print("Good evening")
    elif number < 22:
        print("Nearly bedtime")
    elif number == 23:
        print("Good night!")

if __name__ == "__main__":
    main()