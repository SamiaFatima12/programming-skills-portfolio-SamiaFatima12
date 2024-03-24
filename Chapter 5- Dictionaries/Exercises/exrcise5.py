# Make several dictionaries representing different pets
pet1 =  {'animal': 'dog', 'owner': 'Ayesha'}
pet2 =  {'animal': 'cat', 'owner': 'umar'}


# Store the dictionaries in a list called pets
pets = [pet1, pet2,]

# Loop through the list and print everything known about each pet
for pet in pets:
    print("Animal:", pet['animal'].title())
    print("Owner:", pet['owner'].title())
    print()  # Print a blank line to separate information about each pet