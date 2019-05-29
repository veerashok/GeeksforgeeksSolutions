#include <stdio.h>
#include <stdlib.h>
struct node
{
	int data;
	struct node *next;
	
};

struct node *createNode(int data){

		struct node *q; 

		q = malloc(sizeof(struct node)); 

		q->data = data;
		q->next = NULL;

		return q;

}

int main()
{
	struct node **headRef; 

	printf("Please enter a value\n");
	scanf("%d", &data);
	q = createNode(data); 

	printf("%d\n", q->data);

}