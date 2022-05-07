# Find the highest bidder using dictionaries:
from art import logo

print(logo)
bidding_record = {}
bidding_finished = False

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"{winner} is the highest bidder with the bid amount of {bid_amount}")

while not bidding_finished:
    name = input("Enter your name: ")
    price = int(input("Enter your price: "))
    bidding_record[name] = price
    continue_bidding = input("Enter 'Yes' to continue bidding or 'No' to exit ? ").lower()
    if continue_bidding == "no":
        bidding_finished = True
        find_highest_bidder(bidding_record)
    elif continue_bidding == "yes":
       bidding_finished


