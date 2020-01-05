import re

x = "I am a teacher,I am man, and I am 38 years old.I am not a busInessman."
print(x)
pattern = re.compile(r'(?:[\w])I(?:[\w])')
while True:
    result = pattern.search(x)
    if result:
        if result.start(0) != 0:
            x = x[:result.start(0) + 1] + 'i' + x[result.end(0) - 1:]
        else:
            x = x[:result.start(0)] + 'i' + x[result.end(0) - 1:]
    else:
        break
print(x)
