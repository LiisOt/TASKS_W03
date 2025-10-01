# Prompt user to insert
# A word
# A character
# Find if the character exists in the word. Possible prints below.
# Word "{WordFirst}" contains character "{Character}"
# Word "{WordFirst}" doesn't contain character "{Character}"
# Prompt user to insert one more word
# Compare the first word to the second word. Examples below:
# The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
# The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
# Both inserted words are the same alphabetically, "{WordFirst}"


# Program starting.
print("Program starting.")
# String comparisons
print("String comparisons")
# Insert first word: beans
FirstWord = input("Insert first word: ")
# Insert a character: n
Character = input("Insert a character: ")
if(Character)in(FirstWord):
    print(f'Word "{FirstWord}" contains character "{Character}"')
else:
   print(f"Word \"{FirstWord}\" doesn't contain character \"{Character}\"")
# Word "beans" contains character "n"
# Insert second word: banana
SecondWord = input("Insert second word: ")
if FirstWord < SecondWord:
    print(f'The first word "{FirstWord}" is before the second word "{SecondWord}" alphabetically.')
elif FirstWord > SecondWord:
    print(f"The second word \"{SecondWord}\" is before the first word \"{FirstWord}\" alphabetically.")
else:
    print(f'Both inserted words are the same alphabetically, "{FirstWord}"')
# The second word "banana" is before the first word "beans" alphabetically.
# Program ending.
print("Program ending.")