x = int(input("Number pls: "))

octal = list(str(x))
octal.reverse()
dec = 0
base = 8
for i in range(0,len(octal)):
    x = int(octal[i])*(base**i)
    dec += x




n = dec

x = n

k = []

while (n > 0):
    
    a = int(float(n % 2))
    
    k.append(a)
    
    n = (n - a)/2
    
k.append(0)

s = ""

for j in k[:: -1]:
    
    s = s + str(j)
    
print(s)
