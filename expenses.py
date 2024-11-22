expenses = [10.50, 8, 5, 15, 20, 5, 3]

expenses_total = 0


total = sum(expenses)

for x in expenses:
    expenses_total = expenses_total + x

print('You spent $', expenses_total, sep = '')


print('You spent $', total, sep = '')

