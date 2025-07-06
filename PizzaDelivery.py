print("Welcome to Pizza deliveries!")
size = input("What size pizza do you wan? S, M or L:")
pepperoni = input("What pepperoni do you wan? Y or N?")
cheese = input("What cheese do you wan? Y or N?")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill +=25

if pepperoni =="Y":
    if size == "S":
        bill +=2
    else:
        bill +=3
if cheese =="Y":
    if size == "S":
        bill +=1
print(f"Your final bill: ${bill}.")


