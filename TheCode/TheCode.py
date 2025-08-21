#Prices
bubblegum = 2.0
toffee = 0.2
ice_cream = 5.0
milk_chocolate = 4.0
doughnut = 2.5
pancake = 3.2

#Introduction
print("Welcome to the shop!")
print()

print("These are our prices!")
print("Bubblegum: $2")
print("Toffee: $0.2")
print("Ice cream: $5")
print("Milk chocolate: $4")
print("Doughnut: $2.5")
print("Pancake: $3.2")
print()

cost = 0.0
what = input("Please tell me what you want to purchase: ")

if what == "Bubblegum":
    amount = int(input("Please tell me how much bubblegum to bubble: "))
    bubblegum = amount * bubblegum
    cost = cost + bubblegum

if what == "Toffee":
    amount = int(input("Please tell me how much toffee: "))
    toffee = amount * toffee
    cost = cost + toffee

if what == "Ice cream":
    amount = int(input("Please tell me how much ice cream: "))
    ice_cream = amount * ice_cream
    cost = cost + ice_cream

if what == "Milk chocolate":
    amount = int(input("Please tell me how much milk chocolate: "))
    milk_chocolate = amount * milk_chocolate
    cost = cost + milk_chocolate

if what == "Doughnut":
    amount = int(input("Please tell me how much doughnut: "))
    doughnut = amount * doughnut
    cost = cost + doughnut

if what == "Pancake":
    amount = int(input("Please tell me how much pancake: "))
    pancake = amount * pancake
    cost = cost + pancake


print("This will make:", cost, "dollars.")
print()
print("Have a nice day!")

