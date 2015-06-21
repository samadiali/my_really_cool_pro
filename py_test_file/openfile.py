import re
import os

names_file = open ("lovely.txt")
data = names_file.read()
names_file.close()

#print (data)

#print(re.search(r'Love',data))
print(re.findall(r'\w*-\d*',data))
print(re.findall(r'\d{3}\s\d{3}-\d{4}',data))


print(re.findall(r'''
                 \b@[-\w\d.]* # match a word boundry, an 'at' symbol, and then any number characters
                 [^gov\t]+ # Ignore 1+ instances of the ketters 'g', 'o', or 'v' and a tab
                 \b  # match another word boundry
                 ''', data, re.VERBOSE | re.I))
