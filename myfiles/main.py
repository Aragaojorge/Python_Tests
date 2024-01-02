from calculator import sum

try:
    print(sum('15', 15))
except AssertionError as e:
    print(f'Invalid sum: {e}')
    
print('Sum', sum(25, 25))