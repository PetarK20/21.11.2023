#update се използва за добавяне на елементи от други итеруеми обекти (като списъци, кортежи и др.) 
n = int(input())
my_set = set()

for _ in range(n):
    words = input().split()
    my_set.update(words)
print("\n")
for word in my_set:
    print(word)
