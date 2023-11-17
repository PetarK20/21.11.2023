n = int(input())

my_set1 = set()
odd_num = set()
even_num = set()

for i in range(n):
    names = input()
    for word in input():
        my_set1.update(names)

    sum =  sum(ord(ch) for ch in names)
    
    if sum % 2 == 0:
        sum.add(even_num)
    else:
        sum.add(odd_num)


sum_set = sum(odd_num) + sum(even_num)
if sum(odd_num) == sum(even_num):
    print(sum_set, " - ", sum_set)

if sum(odd_num) > sum(even_num):
    print(sum(odd_num), " - ", sum(even_num))

if sum(even_num) > sum(odd_num):
    print(sum(even_num), " - ", sum(odd_num))

