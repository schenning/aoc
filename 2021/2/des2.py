with open('input.txt') as f:
    data = f.readlines()
inst= []
for elem in data: 
    inst.append(elem.rstrip())

#inst =  (sorted(inst))
down = []
up = []
forw = []
aim = 0  
for elem in inst: 
    if elem[0] == 'd':
        aim += int(elem[-1])
    if elem[0] == 'u':
        aim -= int(elem[-1])
    if elem[0] == 'f':
        forw.append(int(elem[-1]))
        down.append(int(elem[-1])*aim)

    print ((down), (forw), aim)
print((sum(down)-sum(up)) * sum(forw))
