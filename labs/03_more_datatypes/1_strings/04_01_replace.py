'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''



word = input("Tell me a word.")
symbol = input("Tell me a symbol.")
to_replace = word[0]

print(word.replace(to_replace,symbol))











