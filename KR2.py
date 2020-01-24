f = open('mat_dv.txt')
d={}
d1={}
d2={}
max=0
max_1=0
max_2=0
for i in f:
    l=i.split()
    maxi=int(l[3])+int(l[4])
    if maxi>=max:
        max=maxi
        name=l[0]+' '+l[1]
        d[int(l[2])]=(name+' '+ str(max))
    max_a=int(l[3])
    max_g=int(l[4])
    if max_a>=max_1:
        max_1=max_a
        name=l[0]+' '+l[1]
        d1[int(l[2])]=(name+' '+ str(max_1))
    if max_g>=max_2:
        max_2=max_g
        name=l[0]+' '+l[1]
        d2[int(l[2])]=(name+' '+ str(max_2))


print('Победитель в 8-х классах:',d.get(8))
print('Победитель в 9-х классах:',d.get(9))
print('Победитель в 10-х классах:',d.get(10))
print('Победитель в 11-х классах:',d.get(11))
print()
print('Максимум по алгебре в 8-х классах:',d1.get(8))
print('Максимум по алгебре в 9-х классах:',d1.get(9))
print('Максимум по алгебре в 10-х классах:',d1.get(10))
print('Максимум по алгебре в 11-х классах:',d1.get(11))
print()
print('Максимум по геометрии в 8-х классах:',d2.get(8))
print('Максимум по геометрии в 9-х классах:',d2.get(9))
print('Максимум по геометрии в 10-х классах:',d2.get(10))
print('Максимум по геометрии в 11-х классах:',d2.get(11))