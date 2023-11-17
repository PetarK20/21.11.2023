n = int(input())
max_set = set()

for i in range(n):
    common = input().split("-")
    r1 = common[0].split(",")
    r2 = common[1].split(",")
    
    set1 = {x for x in range(int(r1[0]), int(r1[1])+1)}
    set2 = {x for x in range(int(r2[0]), int(r2[1])+1)}

    common1 = set1.intersection(set2)
    
    if len(common1) > len(max_set):
        max_set = common1

print(f"Най-дългото сечение е {max_set} с дължина {len(max_set)}")
    
        
    

