import os
galerie = {}
with open('galerie.txt') as f:
    for line in f.readlines():
        line = line.split(" ")
        if line[0] not in galerie.keys():
            galerie[line[0]] = []
        galerie[line[0]] +=[line[1]]

for key in galerie.keys():
    print(key,end=" ")
    print(len(galerie[key]))


