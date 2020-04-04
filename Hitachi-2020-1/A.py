s = str(input())

for i in range(10):
    if "hi" * i == s:
        print("Yes")
        exit(0)

print("No")