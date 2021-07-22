n = int(input())

words = ["korov", "korova", "korovy"]



if 0<=20-n<=10:
    print(n, words[0])
elif n%10 == 1:
    print(n, words[1])
elif n%10 == 2 or n%10 == 3 or n%10 == 4:
    print(n, words[2])
else:
    print(n, words[0])