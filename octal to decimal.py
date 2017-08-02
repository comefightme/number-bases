x = int(input("Number pls: "))

octal = list(str(x))
octal.reverse()
dec = 0
base = 8
for i in range(0,len(octal)):
    x = int(octal[i])*(base**i)
    dec += x

print(dec)

