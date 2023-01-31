n = int(input())


min_num = 0
max_num = n
result = 0

while min_num <=max_num:
    
    mid = (max_num + min_num) // 2
    
    if mid * mid < n:
        min_num = mid +1
        
    else:
        max_num = mid -1
        result = mid
print(result)


