a = int(input())
b = int(input())
c = int(input())
d = int(input())

S = a*100 + b # копеек стоит товар
O = c*100 + d # копеек отдали за товар

e = (O-S)//100 # рублей сдачв
f = O-S-e*100
print(e, f)

