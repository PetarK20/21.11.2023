import math
n = int(input())

counter = 0

my_set1 = set()
odd_num = set()
even_num = set()

for i in range(n):
    names = input()
    counter += 1
    sum1 = sum(ord(ch) for ch in names)
    print(math.floor(sum1 / counter))

    if sum1 % 2 == 0:
        even_num.add(sum1)
    else:
        odd_num.add(sum1)

sum_odd = sum(odd_num)
sum_even = sum(even_num)

if sum_odd == sum_even:
    print(sum_odd, " - ", sum_odd)

if sum_odd > sum_even:
    print(sum_odd, " - ", sum_even)

if sum_even > sum_odd:
    print(sum_even, " - ", sum_odd)

