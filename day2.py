# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # In strings we can write in both double and single quotes
    print("30 days 30 challenges")
    print('30 days 30 challenges')


# Assigning String to Variable:
Hours = "thirty"
print(Hours)

# indexing using String :
Days = "Thirty days"
print(Days[0])
print(Days[1])
print(Days[2])
print(Days[3])
print(Days[4])
print(Days[5])
print(Days[6])

# Range of index in the string
challenge = "I will win"
print(challenge[0:6])
print(challenge[0:])
print(challenge[:6])
print(challenge[-1:])
print(challenge[:-1])

# length of characters
challenge = "I will win"
print(len(challenge))

# strings in lower case
challenge = "I will win"
print(challenge.lower())

# strings in upper case
challenge = "I will win"
print(challenge.upper())

# string concatenation-joining two words
a = "30 Days"
b = "30 Challenges"
c = a + b
print(c)

# Adding space during concatenation
a = "30 Days"
b = "30 Challenges"
c = a + " " + b
print(c)

# casefold()-usage
text = "30 days 30 challenges"
x = text.casefold()
print(x)


# capitalize-Upper case the first letter in this sentence
text = "30 days 30 challenges"
print(text.capitalize())


# find-used to find a word in the sentence
text = "30 days 30 challenges"
x = text.find("days")
print(x)

# isalpha()-returns True if all the characters are alphabet letters (a-z)
text = "30 days 30 challenges"
x = text.isalpha()
print(x)

# isalnum()-returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
text = "30 days 30 challenges"
x = text.isalnum()
print(x)