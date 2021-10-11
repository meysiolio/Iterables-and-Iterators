from itertools import combinations

n = int(input())
letters = ''.join(input().split())
k = int(input())

count = 0

for i in list(combinations(letters,k)):
    if 'a' in i:
        count += 1
        
print(count / (len(list(combinations(letters,k)))))