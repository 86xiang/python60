import re

x = 'This is a a desk.'
pattern = re.compile(r'\b(\w+)(\s+\1){1,}\b')
matchResult = pattern.search(x)
x = pattern.sub(matchResult.group(1), x)
print(x)

'''
x = 'This is a a desk.'
pattern = re.compile(r'(?P<f>\b\w+\b)\s(?P=f)')
matchResult = pattern.search(x)
x = x.replace(matchResult.group(0), matchResult.group(1))
'''
