import os

# Read translations from file
with open('fr2en.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

translations = {}
for line in lines:
    fr, en = line.strip().split(': ')
    translations[fr] = en
# print(translations)
# Specify the subdirectory
subdirectory = 'symbols'

# Rename files in subdirectory and its subdirectories
for dirpath, dirnames, filenames in os.walk(subdirectory):
    for filename in filenames:
        # print(filename)
        if filename in translations:
            print("translating " + filename + " to " + translations[filename] )
            os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, translations[filename]))
