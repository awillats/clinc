import re 

print(re.escape('@'))

with open('test.txt','r') as f:
    s = f.read()
    print(re.search('\[@',s))