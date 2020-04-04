W, H, x ,y ,r = map(int, input().split())

word = "Yes"

if x < 0 or y < 0:
    word = "No"

if (x + r) > W:
    word = "No"

if (x - r ) < 0:
    word = "No"

if (y + r) > H:
    word = "No"

if (x - r ) < 0:
    word = "No"

print(word)