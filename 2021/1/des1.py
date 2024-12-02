with open('input.txt') as f: 
    depth = f.readlines()

# Part 1
cnt = 0

"""for i in range(len(depth)-1):
    if int(depth[i+1]) - int(depth[i]) > 0:
        cnt += 1 
print (cnt)i"""

# Part 2

cnt = 0
a = 0
#for i in range(0,len(depth)-3,3):
#    print (int(depth[i]) + int(depth[i+1]) + int(depth[i+2]))
for i in range(0,len(depth)-3,3):
    for j in range(3):
        print (i, int(depth[i+j]) +int(depth[i+j+1]) + int(depth[i+j+2]))
        if a-(int(depth[i+j]) +int(depth[i+j+1]) + int(depth[i+j+2]))<0:
            cnt+=1
        a=int(depth[i+j]) +int(depth[i+j+1]) + int(depth[i+j+2])
        print ('cnt', cnt)
        print 
        
