
# Part 1
col1, col2 = [], []
total_dist = 0
with open('input_d1.txt') as f:
    for line in f:
        a, b = map(int, line.split())
        col1.append(a)
        col2.append(b)

#col1 = [3,4,2,1,3,3]
#col2 =  [4,3,5,3,9,3]

c1 = sorted(col1)
c2 = sorted(col2)

for i in range(len(c1)):
    dist = abs(c1[i] - c2[i])
    total_dist += dist

print (total_dist)

# Part 2
sim_score = 0
for n in c1: 
    for m in c2: 
        if n==m:
            sim_score += n
     
print (sim_score) 



