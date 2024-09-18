s,e = map(int,input().split())
res = []
for i in range(s,e + 1):
    if i != 1:
        lst = []
        for j in range(1, e + 1):
            if i % j == 0:
                lst.append(j)
        if len(lst) % 2 != 0:
            res.append(i)

print(len(res))
        
