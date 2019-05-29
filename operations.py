

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete all
# three functions
# if the element is found in the list
# function  must return true or else
# return false
def searchEle(a, x):
    try:
        if a.index(x) != -1:
            return True
        else:
            return False
    except:
        return False

def insertEle(a, y, yi):
    if len(a) >= yi:
        a.insert(yi, y)
        return True
    else:
        return False

        
def deleteEle(a, z):
    i = a.index(z)
    if i != 0:
        del a[i]
        return True
    else:
        return 0


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        x,y,yi,z = list(map(int, input().strip().split()))
        if(searchEle(a, x)):
            print('1', end=' ')
        else:
            print('0', end= ' ')
        if(insertEle(a, y, yi)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        if(deleteEle(a, z)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        print()
# Contributed By: Harshit Sidhwa

    