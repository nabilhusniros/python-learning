fruits = ['apple', 'orange', 'banana']
years = [3, "2024", 2.5, 987, "1995"]

print('apple' in fruits)
print(fruits.count('apple'))
print(fruits.index('apple'))

print(fruits, years)

fruits.append('grapes')
print(fruits)

fruits.extend(years)
print(fruits)

fruits.remove('grapes')
print(fruits)

fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

numbers = [5, 123, 6, 45, 5.65]
numbers.sort()
print(numbers)
