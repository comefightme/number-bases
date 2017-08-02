dec = int(input("Number: "))

x = list(str(dec))

x.reverse()

ans = 0

base = 2

for i in range(len(x)):
        dec = int(x[i])*(base**i)
        ans += dec



x = ans

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
