n = int(input())

cards = []
v = ["S", "H", "C", "D"]
number = list(range(1,14))

for i in v:
    for num in number:
        cards.append("{} {}".format(i, num))

my_cards = []
if n == 52:
    exit(0)
    
for i in range(n):
    my_cards.append(input())

# https://qiita.com/Toitu_Prince/items/222b50594b4bb7b189ee
result = [i for i in cards if i not in my_cards]
print("\n".join(map(str, result)))

    