bases = {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8',\
         '9':'9','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}



x = int(input("Number pls: "))

num = int(x)
hexa = []
s = ''
while (num > 0):
    rem = num % 16
    hexa.append(bases[str(rem)])
    num = num // 16
hexa.reverse()

for i in hexa:
    s = s + str(i)

print(s)
