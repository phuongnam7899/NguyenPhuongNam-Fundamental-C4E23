from pymongo import MongoClient
from matplotlib import pyplot
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client=MongoClient(uri)
data_base= client.get_database()
customers= data_base["customers"]
cus_list=customers.find()
checked=[]
ref_list=[]
ref_count=[]
for customer in cus_list:
    ref_list.append(customer["ref"])
for ref in ref_list:
    while True:
        if ref in checked:
            break
        else:
            ref_count.append(ref_list.count(ref))
            checked.append(ref)
pyplot.pie(ref_count,labels=checked,autopct="%.1f%%",shadow=True)
pyplot.axis("equal")
pyplot.title("Percentage of customer's references")
pyplot.show()
           
