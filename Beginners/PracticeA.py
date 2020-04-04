args=[input() for i in range(3)]

print (int(args[0]) + sum(map(int,args[1].split())))
print (args[2])
