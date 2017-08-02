dec = int(input("Number: "))

x = list(str(dec))

x.reverse()

ans = 0

base = 2

for i in range(len(x)):
        dec = int(x[i])*(base**i)
        ans += dec


print(ans)
