k = int(input())
hours = k // 3600
minutes = (k - hours*3600) // 60
print(f'It is {hours} hours {minutes} minutes.')
