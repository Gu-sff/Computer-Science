
d = {"a": 3, "b": 5, "c": 4, "C": 2}

del d["a"]
k = d.keys()
v = d.values()
k1 = d.items()
print(sorted(d))
print(k)
print(sorted(v))

sk0 = sorted(d.items())
sk = dict(sorted(d.items()))

#______________________________________________________________
sv = sorted(d.items(), key=lambda x: x[1])
sv1 = sorted(d.items(), key=lambda x: x[1], reverse=True)

print(sk0)

print(sk)
print(dict(sv))
print(sv1)

print("\n")


a = [(1, 2), (1, 4), (3, 5), (6, 1)]
nList = list()
anyList = list()
for item in a:
    if item[0] == 1:
        nList.append(item)
for item1 in a:
    for i in range(len(item1)):
        if item1 not in anyList:
            if item1[i] == 1:
                anyList.append(item1)
print(nList)
print(anyList)

resultFirst1 = [item for item in a if item[0] == 1]
print(resultFirst1)
resultAny1 = [item for item in a if 1 in item]
print(resultAny1)


print("\n")


#______________________________________________________________
toNumberList = ["1", "2", "3"]
newList = [int(i) for i in toNumberList]

toStringList = [4, 5, 6]
print(",".join(toNumberList))
newList1 = [str(i) for i in toStringList]
print(newList)
print(newList1)

#______________________________________________________________
print(round(5.62 , 1))
kkk = 1, 2, "yes"
print(kkk)


counts = [
[ 0, 3, 0 ],
[ 0, 0, 1 ],
[ 0, 0, 1 ],
[ 1, 0, 0 ],
[ 0, 0, 1 ],
[ 3, 1, 1 ],
[ 0, 1, 0 ],
[ 1, 0, 1 ]
]

total = "total"
price = 123.00
total1 = "sadsafasfas"
price1 = 12313
print("%-15s" % (total) ,price)
print("%-15s" % (total1), price1)


sdj ="12324214"
for i in range(len(sdj)):
    print(sdj[i])



