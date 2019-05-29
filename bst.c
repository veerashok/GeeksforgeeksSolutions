#include <stdio.h>
#include <stdlib.h>

struct bstNode
{
	struct bstNode *left;
	int data;
	int freq; 
	struct bstNode *right; 
};

struct bstNode *createNode(int val){

		struct bstNode *q=NULL;

		q = (struct bstNode*)malloc(struct bstNode*);

		q->left = NULL;
		q->right = NULL;

		q->freq = 1;
		q->data = val;

}


