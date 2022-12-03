with open('input1.txt', 'r') as f:
    cals = f.read()


cals = [c.split('\n') for c in cals.split('\n\n')]
sums = []

for elem in cals:
    s = sum([int(i) for i in elem])
    sums.append(s)
sums.sort()

# pb1: 
print(sums[-1]) 

# pb2: 
print (sums.pop() + sums.pop() + sums.pop())
