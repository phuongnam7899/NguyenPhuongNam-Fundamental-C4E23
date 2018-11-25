import mlab_connect
from movies import Movie
from resource import Resource
from faker import Faker
from random import randint

faker = Faker("en_US")
# for _ in range(5):
#     print(faker.state)



mlab.connect()

# movie_list = Movie.objects()

# for m in movie_list:
    # print(m.image)


# resource_list = Resource.objects()

# for r in resource_list:
#     print(r.name,r.city,r.yob,r.height,r.weight)


# m = Movie.objects().with_id("5bf7fd262efee2059008b9de")
# m.delete()


# r = Resource.objects().with_id("5bf7fe0e2efee204f0fe2634")
# if r == None:
#     print("NFound")
# else:
#     print("Found")
#     r.delete()


# m = Movie(title="batman",year="2005",image="https://www.dccomics.com/sites/default/files/GalleryChar_1920x1080_BM_Cv38_54b5d0d1ada864.04916624.jpg")
# m.save()


# r1 = Resource(name="ironman",city="NY",yob=1990,weight=60,height=180)
# r2 = Resource(name="captain",city="NY",yob=1991,weight=70,height=181)
# r3 = Resource(name="antman",city="NY",yob=1992,weight=80,height=182)
# r1.save()
# r2.save()
# r3.save()


# r_list = Resource.objects()
# r = r_list[0]
# r.delete()


# r= Resource.objects().first()
# r.delete()


for _ in range(200):
    name = faker.name()
    city = faker.state()
    yob = randint(1953,2000)
    height = randint(150,200)
    weight = randint(40,150)
    r = Resource(name=name,city=city,yob=yob,height=height,weight=weight)
    r.save()


# records = Resource.objects(city="New York")
# print(len(records))
# records_height = Resource.objects(height=172)
# for r_height in records_height:
#     print(r_height.name)


# records_height = Resource.objects(name__contains="Paul")
# for r in records_height:
#     print(r.name)

# records= Resource.objects(height__gt=170,weight__lte=70,name__contains="T")
# for r in records:
#     print(r.name)


# records = Resource.objects()

# for r in records:
#     r.update(set__available=False)

r= Resource.objects().with_id("5bf80cc12efee20a44685526")
r.update(set__available= True)





