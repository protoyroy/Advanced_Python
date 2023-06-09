num = int(input('Enter your number\n'))
table = [num * i for i in range (1,11)]
# print(table)

formatted = [f"{num} x {i} = {table[i-1]}" for i in range(1,11)]
print(*formatted, sep='\n')