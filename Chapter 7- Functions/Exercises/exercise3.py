def make_shirt(size, message):
    """Prints a summary of the shirt size and message."""
    print("The shirt size is " + size + " and the message printed on it is: " + message)

# Call the function with positional arguments
make_shirt("Large", "I love pyhton")

# Call the function with keyword arguments
make_shirt(size="Medium", message="Hello, world Im student of cybersecurity")