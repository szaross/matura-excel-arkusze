import os
galerie = {}
with open('galerie.txt') as f:
    for line in f.readlines():
        line = line.split(" ")
        #print("a")
        if line[1] not in galerie.keys():
            galerie[line[1]] = {}
            #print("b")
        pole = 0
        liczba_galerii=0
        i=2
        #print("c")
        while(i!=0):
            pole = pole + (int(line[i])*int(line[i+1]))
            liczba_galerii +=1
            i+=2
            #print(i)
            if i==140 or int(line[i+1]) == 0 :
                i=0
                

        galerie[line[1]]["pole"]=pole
        galerie[line[1]]["liczba_gal"]=liczba_galerii

# print(galerie)

# for key in galerie.keys(): ZADANIE 1
#     print(key,end=" ")
#     print(galerie[key]["pole"],end=" ")
#     print(galerie[key]["liczba_gal"])

minp = galerie[list(galerie.keys())[0]]['pole'] #pole
minm = list(galerie.keys())[0] #miasto

maxp = galerie[list(galerie.keys())[0]]['pole'] #pole
maxm = list(galerie.keys())[0] #miasto
for key in galerie.keys():
    if galerie[key]['pole']<minp:
        minp = galerie[key]['pole'] #pole
        minm = key #miasto
    elif galerie[key]['pole']>maxp:
        maxp = galerie[key]['pole'] #pole
        maxm = key #miasto

print(maxm+" "+str(maxp))
print(minm+" "+str(minp))




