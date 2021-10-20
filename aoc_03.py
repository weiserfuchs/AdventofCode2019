x = ["R8","U5","L5","D3"]
y = ["U7","R6","D4","L4"]
t = [[10000],[10000]]
t[5000][4990] = 10
d = 0 
print(t)
for inst in x:
    if inst[:1] == "R":
        pass
    elif inst[:1] == "U":
        d += int(inst[1:])
    elif inst[:1] == "L":
        d += int(inst[1:])
    elif inst[:1] == "D":
        d += int(inst[1:])

print(d)

#d = 0

#for i in range(0,len(x)):
#    d += abs(x[i] - y[i])


#print(d)