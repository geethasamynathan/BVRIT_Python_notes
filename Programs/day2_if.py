# age=int(input("Enter your age to get movie Ticket "))
# cutomer_type=input("Enter your customer type (VIP/Normal) ")
# if age >= 18:
#     if cutomer_type == "VIP":
#         print("You are eligible to buy ticket with 10% discount")
#     else :
#         print("You are eligible to buy ticket without any discount")
# else :
#     print("You are eligible to watch the movie  not to buy the ticket")



# Example to unpack random values from a tuple
cities=("Delhi","Mumbai","Banglore","Chennai","Kolkata")

# city1,_,city3,_,_= cities

bglcity_index=cities.index("Banglore")
print(cities[bglcity_index])
