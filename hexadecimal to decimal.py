bases = {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8',\
         '9':'9','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}

num = str(input("Number pls: "))
hexa = list(num)
hexa.reverse()
ans = 0
base = 16
for i in range(0,len(hexa)):
    num = int(bases[hexa[i]])*(base**i)
    ans += num

print(ans)
