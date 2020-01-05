import sys
import os

directory = sys.argv[1]
filename = sys.argv[2]
paths = os.walk(directory)
for root, dirs, files in paths:
    if filename in files:
        print('Yes')
        break
else:
    print('No')
