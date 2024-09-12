import os
import art
print(art.logo)

auction_bids = {}

print("Welcome to the secret auction program.")
while True:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))

  auction_bids[name] = bid
  
  bidders = input("Are there any other bidders? Type 'yes' OR 'no'.\n").lower()
  if bidders == "yes":
    os.system('cls' if os.name == 'nt' else 'clear')
    
  elif bidders == "no":
    highest_bider = max(auction_bids, key=auction_bids.get)
    highest_bid = auction_bids[highest_bider]
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The winner is {highest_bider} with a bid of ${highest_bid}")
    break

