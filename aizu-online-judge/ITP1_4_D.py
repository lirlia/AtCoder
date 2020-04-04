n = int(input())
l =[]
for i in range(n):
    l.append(int(input()))

print(min(l), max(l), sum(l)/len(l))