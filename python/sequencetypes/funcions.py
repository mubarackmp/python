a = "Hello"
print(a)

# Slicing
b = "Hello, World!"
print(b[2:5])
# Slice From the Start
b = "Hello, World!"
print(b[:5])

# MODIFY STRINGS
a = "Hello, World!" 

# Upper Case
print(a.upper())

# Lower Case
print(a.lower())

# Remove Whitespace(IS USING TO REMOVE THE SPACES WHICH IS IN BEFORE AND AFTER THE STRING)
print(a.strip())

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
d = a + " " + b
print(d)

# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
