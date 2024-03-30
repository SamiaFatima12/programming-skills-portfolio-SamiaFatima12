def describe_city(city, country="Default Country"):
    """Prints a sentence describing the city and its country."""
    print(city + " is in " + country + ".")

# Call the function for three different cities
describe_city("KARACHI", "PAKISTAN")
describe_city("IZMIR", "TURKEY")
describe_city("LONDON")