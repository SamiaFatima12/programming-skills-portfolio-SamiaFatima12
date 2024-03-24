toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish):")
    
    if topping.lower() == 'quit':
        break
    else:
        print("Adding", topping, "to your pizza.")
        toppings.append(topping)

print("Your pizza will have the following toppings:")
for topping in toppings:
    print("- " + topping)