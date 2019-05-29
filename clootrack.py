import operator


def getKey1(item):
    return item[0]


def getKey2(item):
    return item[1]


def tweetFrequency(names):
    distinctUsers = list(set(names))
    usersWithFrequency = []

    for x in distinctUsers:
        usersWithFrequency.append((x, names.count(x)))
        
    usersWithFrequency.sort(key=getKey2, reverse=True)
    
    maximumFreq = usersWithFrequency[0][1]
    
    usersWithMaxFrequency = []
    
    for x in usersWithFrequency:
        if x[1] == maximumFreq:
            usersWithMaxFrequency.append(x)
    
    usersWithMaxFrequency.sort(key=getKey1)
    
    for x in usersWithMaxFrequency:
        print(x[0], x[1])


t = int(input())
for _ in range(t):
    n = int(input())
    names = []
    
    for i in range(n):
        name, tweet_id = list(map(str, input().strip().split(" ")))
        names.append(name)
    tweetFrequency(names)
