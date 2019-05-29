#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *next;
	
};

struct node *partition(struct node **headRef, struct node *end);

struct node *tail(struct node **headRef, struct node *end){

	struct node *p=NULL;
	p = *headRef; 

	while ( p->next != NULL && ( end != NULL && p->next->data < end->data )){
		p = p->next;
	}

	return p;

}

struct node *createNode(int data){

		struct node *q; 
 
		q = (struct  node *)malloc(sizeof(struct node *)); 

		q->data = data;
		q->next = NULL;

		return q;

}

void push(struct node **headRef, int val){

	struct node *q=NULL;

	q = createNode(val);

	q->next = *headRef; 

	*headRef = q; 
}

void swapNodes(struct node **head_ref, int x, int y) 
{ 
   // Nothing to do if x and y are same 
   if (x == y) return; 
  
   // Search for x (keep track of prevX and CurrX 
   struct node *prevX = NULL, *currX = *head_ref; 
   while (currX && currX->data != x) 
   { 
       prevX = currX; 
       currX = currX->next; 
   } 
  
   // Search for y (keep track of prevY and CurrY 
   struct node *prevY = NULL, *currY = *head_ref; 
   while (currY && currY->data != y) 
   { 
       prevY = currY; 
       currY = currY->next; 
   } 
  
   // If either x or y is not present, nothing to do 
   if (currX == NULL || currY == NULL) 
       return; 
  
   // If x is not head of linked list 
   if (prevX != NULL) 
       prevX->next = currY; 
   else // Else make y as new head 
       *head_ref = currY;   
  
   // If y is not head of linked list 
   if (prevY != NULL) 
       prevY->next = currX; 
   else  // Else make x as new head 
       *head_ref = currX; 
  
   // Swap next pointers 
   struct node *temp = currY->next; 
   currY->next = currX->next; 
   currX->next  = temp; 
} 

void printArray(struct node **headRef){
	struct node *p=NULL;
	p = *headRef;

	int i = 0;

	while(p != NULL){
		printf("%d ", p->data);
		p = p->next;
		i += 1;

		if(i == 9){
			break;
		}

	}
	printf("\n");
}

void quickSortRecurr(struct node **headRef, struct node *pi){
	struct node *p=NULL;

	p = *headRef;

	struct node *end=NULL;

	end = pi;

	pi = partition(&p, end);


	struct node *r_pivot=NULL;
	r_pivot = pi->next;
	
	end = pi;


	quickSortRecurr(&p, pi);
	quickSortRecurr(&r_pivot, pi);


}

void quickSort(struct node **headRef ){
	struct node *pi=NULL;
	struct node *p=NULL;
	p = *headRef;

	quickSortRecurr(&p, pi);

}
struct node *partition(struct node **headRef, struct node *end){
	struct node *p=NULL;
	struct node *pi=NULL;
	struct node *i=NULL;
	struct node *pivot=NULL;
	struct node *t=NULL;

	p = *headRef;

	t = tail(&p, end);	

	pivot = t->next;

	int j = 0;

	while(p->next != NULL){

		printf("I am here %d\n", p->data);

		if(p->data < pivot->data){

			if(j == 0){
				i = *headRef;
				j++;
			}
			else{
				i = i->next;
				swapNodes(&p, i->data, p->data);

			}
		}

		p = p->next;
	}

	swapNodes(&p, i->data, pivot->data);

	return i->next;


}

int main()
{
	struct node *head=NULL; 
	struct node *q=NULL; 
	struct node *p=NULL;


	int data;
	int n, t, num; 


	printf("Inseting values.... \n");

	scanf("%d", &t);


	while(t--){
		scanf("%d", &n);

		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &num);
			push(&head, num);
		}
	}

	printArray(&head); 
	quickSort(&head);
	printArray(&head);

}