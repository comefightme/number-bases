x = int(input("Number pls: "))

ans = []

while (x > 0):
    rem = x % 8
    ans.append(str(rem))
    x = x // 8


ans.reverse()

s = ''

for i in ans:
    s = s + str(i)

print(s)
