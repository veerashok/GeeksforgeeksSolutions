def queryReplies(arr, query_arr, n, q):
    
    rankArray = [ ]
    
    for i in range(0,len(arr), 2):
        rankArray.append((arr[i], arr[i+1] - arr[i] + 1))
    
    
    
    for x in query_arr:
        i = 0
        rank = x
        sum = 0
        for t in rankArray:
            rank = rank - t[1]
            if rank > 0:
                sum += t[1]
                i += 1
            else:
                break
        
        temp = rankArray[i]
        print(temp[0] + x - sum -1)
        
        
        #print(temp[0])
        
        
        
        
        
        
t = int(input())
for _ in range(t):
    n, q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    query_arr = list(map(int, input().split()))
    queryReplies(arr, query_arr, n, q)
    