
col1, col2 = [], []
total_dist = 0
with open('input.txt') as f:
    for line in f:
        a, b = map(int, line.split())
        col1.append(a)
        col2.append(b)

c1 = sorted(col1)
c2 = sorted(col2)

for i in range(len(c1)):
    dist = abs(c1[i] - c2[i])
    total_dist += dist

print (total_dist)



