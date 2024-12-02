from statistics import mode

with open('input.txt') as f:
    data = f.readlines()

#### Part 1
code = []
gamma = ''
eps = []
for elem in data: 
    code.append((list(elem.rstrip())))
for i in range(12):

    c = [col[i] for col in code]
    gamma += str(mode(c))


for elem in list(gamma):
    eps.append( (str((int(elem) +1)%2)))

eps = ''.join(eps)
eps = int(eps,2)
gamma =  (int(gamma,2))

print(gamma*eps)

##### Part 2

 
code=[]
for elem in data: 
    code.append(''.join((list(elem.rstrip()))))



print(code)
