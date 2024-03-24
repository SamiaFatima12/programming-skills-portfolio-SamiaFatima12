location = [ 'paris', 'maldives', 'makkah', 'finland']

print("original location")
print(location)

print("\nalphabetical")
print(sorted(location))

print("\noriginal order:")
print(location)

print("\nreverse alphabetical:")
print(sorted(location, reverse=True))

print("\noriginal order:")
print(location)

print("\nreversed:")
location.reverse()
print(location)

print("\noriginal order:")
location.reverse()
print(location)
print("\nAlphabetical")
location.sort()
print(location)

print("\nreverse alphabetical")
location.sort(reverse=True)
print(location)