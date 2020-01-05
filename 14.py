import re

x = input('Please input a string:')
pattern = re.compile(r'\b[a-zA-Z]{3}\b')
print(pattern.findall(x))
