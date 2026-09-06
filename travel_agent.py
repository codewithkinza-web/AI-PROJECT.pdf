place = input("Enter destination (Dubai, Turkey, Malaysia): ")
budget = int(input("Enter your budget: "))

if place == "Dubai":
    if budget >= 150000:
        print("Flight available for Dubai!")
    else:
        print("Your budget is not enough for Dubai.")

elif place == "Turkey":
    if budget >= 180000:
        print("Flight available for Turkey!")
    else:
        print("Your budget is not enough for Turkey.")

elif place == "Malaysia":
    if budget >= 120000:
        print("Flight available for Malaysia!")
    else:
        print("Your budget is not enough for Malaysia.")

else:
    print("Destination not available.")