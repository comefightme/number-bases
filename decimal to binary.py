n = int(input("Number: "))

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
