# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import re
def allowed_specified_char(string):
    charR = re.compile(r'[^a-zA-Z0-9.]')
    string =charR.search(string)
    return not bool(string)
print(allowed_specified_char("ABC123"))
print(allowed_specified_char("156*#"))
print(allowed_specified_char("azby"))

import re
def text_search(text):
    patterns='ab'
    if re.search(patterns, text):
        return "Matched"
    else :
        return "Not Matched"
print(text_search("absolute"))
print(text_search("bass"))

import re
def end_num(string) :
    text=re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False
print(end_num('B16'))
print(end_num('bhavi16'))

import re
results=re.finditer(r"([0-9]{1,3})","Example number 20,35,46,57,100 is important")
print("Numbers of length 0 to 3")
for n in results:
    print(n.group(0))

import re
def text_match(string):
    text=re.compile(r".*[A-Z]")
    if text.match(string):
        return True
    else:
        return False
print(text_match("bhavi"))
print(text_match("vicky"))













