from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

other_bidders = True
bidders = []

print(logo)

while(other_bidders):
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = input("What is your bid? $")

    bidders.append({"name": name, "bid": bid})

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if(more_bidders == "no"):
        other_bidders = False
        aux_bid = 0
        aux_name = ""
        for winner in bidders:
            if(int(winner["bid"]) > aux_bid):
                aux_bid = int(winner["bid"])
                aux_name = winner["name"]
        print(f"The winner is {aux_name} with ${aux_bid}.")
    else:
        clear()

