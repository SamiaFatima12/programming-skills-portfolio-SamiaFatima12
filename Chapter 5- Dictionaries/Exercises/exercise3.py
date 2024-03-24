glossary = {
    'variable': 'a reserved memory location to store values.',
    'function': 'a block of code which only runs when it is called.',
    'loop': 'repeating something over and over until a particular condition is satisfied.',
    'list': 'creates a collection that can be manipulated for your analysis',
    'tuple': 'a built-in data type that allows you to create immutable sequences of values',
    }

for term, definition in glossary.items():
    print(term.capitalize() + ':')
    print(definition)
    print()  # Insert a blank line between each word-meaning pair