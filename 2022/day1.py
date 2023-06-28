ElfInv = "2022\day1.txt"
f = open(ElfInv, 'r')
sum = 0
mostCalories = 0
listaInv = []
topInv = []
for line in f:
    if line == "\n":
        listaInv.append(sum)
        sum = 0
    else:
        sum += int(line)
f.close()
listaInv.sort()
sizeInv = len(listaInv)
print(listaInv[sizeInv-1]+listaInv[sizeInv-2]+listaInv[sizeInv-3])
 
