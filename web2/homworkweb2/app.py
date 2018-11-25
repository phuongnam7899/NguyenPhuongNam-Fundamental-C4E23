import mlab
from river import River
mlab.connect()
#1
print("Rivers in Africa continent:")
africa_rivers = River.objects(continent="Africa")
for river in africa_rivers:
    print(river.name)

#2
print("River in S.America with length less than 1000km:")
samerica_lt1000km = River.objects(continent="S. America", length__lt=1000)
for river in samerica_lt1000km:
    print(river.name,":",river.length,"km")