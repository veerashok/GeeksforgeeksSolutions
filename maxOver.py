import sys 

def maxOverlap(start,end): 

	n= len(start) 
	maxa = max(start)# Finding maximum starting time 
	maxb = max(end) # Finding maximum ending time 
	maxc=max(maxa,maxb) 
	x =(maxc+2)*[0]
	print(x)
	cur=0; idx=0

	for i in range(0,n) :# CREATING AN AUXILIARY ARRAY 
		x[start[i]]+=1 # Lazy addition 
		x[end[i]+1]-=1

	print(x)
	maxy=-1
	#Lazily Calculating value at index i 
	for i in range(0,maxc+1): 
		cur+=x[i] 
		if maxy<cur : 
			maxy=cur 
			idx=i	 
	print("Maximum value is: {0:d}".format(maxy), 
					" at position: {0:d}".format(idx)) 
if __name__ == "__main__": 
	
	start=[13,28,29,14,40,17,3] 
	end=[107,95,111,105,70,127,74] 
					
	maxOverlap(start,end) 
