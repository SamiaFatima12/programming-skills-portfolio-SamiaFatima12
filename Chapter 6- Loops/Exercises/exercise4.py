sandwich_orders = [ 'egg and cheese', 'hot chicken', 'beef']
finished_sandwiches = []

# Loop through each sandwich order
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Take the first sandwich order
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich.capitalize())