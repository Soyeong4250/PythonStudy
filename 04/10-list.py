names = ["홍길동","이순신", "이세종"]
a = []
b = list()
a.append("남박사")
a.append("김박사")
a.append("가가멜")
# a.remove("가가멜")
# a.remove("김길동")
b = a.pop("가가멜")

print(names, a, b)
del a[1]

print(names, a, b)

print(names[2])
print(names[0:2])