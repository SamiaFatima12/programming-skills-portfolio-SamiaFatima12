rivers = {
    'indus': 'northern Pakistan',
    'Jhelum ': 'Azad Kashmir',
    'Sutlej': 'Himachal Pradesh'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country}.")

print("\nList of rivers:")
# Print the name of each river
for river in rivers.keys():
    print(river.capitalize())

print("\nList of countries:")
# Print the name of each country
for country in rivers.values():
    print(country)