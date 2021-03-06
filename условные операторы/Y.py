'''
Билет на одну поездку в метро стоит 15 рублей,
билет на 10 поездок стоит 125 рублей,
билет на 60 поездок стоит 440 рублей.
Пассажир планирует совершить n поездок.
Определите, сколько билетов каждого вида он должен приобрести,
чтобы суммарное количество оплаченных поездок было не
меньше n, а общая стоимость приобретенных билетов – минимальна.
'''

n = int(input())

sum = 0
count_60=0
count_10=0
count_1=0

while n>=35:
    n -= 60
    sum += 440
    count_60 += 1

while n>=9:
    n -= 10
    sum += 125
    count_10 += 1

while n>=1:
    n -= 1
    sum += 15
    count_1 += 1

print(count_1, count_10, count_60)