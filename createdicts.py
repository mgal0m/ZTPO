import csv

with open('a.csv') as f:
    dictA = dict(filter(None, csv.reader(f)))

with open('b.csv') as g:
    dictB = dict(filter(None, csv.reader(g)))

with open('c.csv') as h:
    dictC = dict(filter(None, csv.reader(h)))

print(dictA)
print(dictB)
print(dictC)








