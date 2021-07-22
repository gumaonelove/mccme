x = int(input())
p = int(input())
y = int(input())
years=0
while x<y:
    years+=1
    x*=(1+(p/100))
    x = int(x*100)/100
print (years)