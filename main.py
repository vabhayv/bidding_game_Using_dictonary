import os

bid = {}
print("Welcome to the secret auction program.")
end_people = False

def bidder_winner(participants):
    high_bid = 0
    win = ""
    for bidder in participants:
        money = participants[bidder]
        if money > high_bid:
            high_bid = money
            win = bidder
    print(f"\n\nThe winner is {win} with a bid of {high_bid}")
while not end_people:
    name = input("what's your name?: ")
    user_bid = int(input("what's your bid?: "))
    bid[name] = user_bid
    people = input("Are there any other bidders? type 'yes' or 'no'. : ")
    if people == 'yes':
        os.system('clear')
        end_people = False
    elif people == 'no':
        end_people = True
        bidder_winner(bid)
        
                