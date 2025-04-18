# Project Name: Med Libs Game
# Date: 18.04.2025
# Author: Sogol Saleki
# Description:
# Features:
# Requirements:

item=input("What is/are the purchases items (in singular)? ")
price=float(input("How much is an item ($)? "))
quantity=int(input("And how many have you bought? "))

total=round((price*quantity), 2)

if quantity==1:
    print(f"You have purchased a/an {item}")
elif quantity>1:
    print(f"You have purchased {quantity} {item}s")
else:
    print("You haven't purchased anything.")
    exit()

print(f"The total price is {total}$")