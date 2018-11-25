from matplotlib import pyplot
#1 prepare data
count=[12,2,2]
#2 prepare labels
name=["a","b","c"]
#3 draw pie
pyplot.pie(count,labels=name,autopct="%.1f%%",shadow= True, explode=[0,0.05,0])
pyplot.title("abcxyz")
pyplot.axis("equal")
#4 show chart
pyplot.show()