L = []
grocery = ["milk", "eggs", "bread"]

print(len(L))
print(len(grocery))

print(grocery[0])
print(grocery[1])
print(grocery[2])
print(grocery[3])

years = [1984, 1986, 1988, 1988]

print(len(years))
print(years.count(1988))
print(years.count(2017))

print(years.index(1986))
print(years.index(1988))
print(years.index(0))

grocery = []
grocery.append("bread")
print(grocery)
grocery.append("milk")
print(grocery)
grocery.insert(1, "eggs")
print(grocery)

fun = ["drone", "vr glasses", "game console"]
grocery.extend(fun)
print(grocery)
grocery.pop()
print(grocery)
grocery.pop(1)
print(grocery)

grocery[0] = "croissant"
print(grocery)
