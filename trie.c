#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define ARRAY_SIZE(a) sizeof(a)/sizeof(a[0])

#define ALPHABET_SIZE (26)

#define CHAR_TO_INDEX(c) ((int)c - (int)'a')


struct TrieNode
{
	struct TrieNode *children[ALPHABET_SIZE]; 
	bool isEndOfWord;
};

struct TrieNode *getNode(void) 
{ 
    struct TrieNode *pNode = NULL; 
  
    pNode = (struct TrieNode *)malloc(sizeof(struct TrieNode)); 
  
    if (pNode) 
    { 
        int i; 
  
        pNode->isEndOfWord = false; 
  
        for (i = 0; i < ALPHABET_SIZE; i++) 
            pNode->children[i] = NULL; 
    } 
  
    return pNode; 
}

void insert(struct TrieNode *root, const char *key) 
{ 
    int level; 
    int length = strlen(key); 
    int index; 
  
    struct TrieNode *pCrawl = root; 
  
    for (level = 0; level < length; level++) 
    { 
        index = CHAR_TO_INDEX(key[level]); 
        if (!pCrawl->children[index]) 
            pCrawl->children[index] = getNode(); 
  
        pCrawl = pCrawl->children[index]; 
    } 
  
    // mark last node as leaf 
    pCrawl->isEndOfWord = true; 
}

bool search(struct TrieNode *root, const char *key) 
{ 
    int level; 
    int length = strlen(key); 
    int index; 
    struct TrieNode *pCrawl = root; 
  
    for (level = 0; level < length; level++) 
    { 
        index = CHAR_TO_INDEX(key[level]); 
  
        if (!pCrawl->children[index]) 
            return false; 
  
        pCrawl = pCrawl->children[index]; 
    } 
  
    return (pCrawl != NULL && pCrawl->isEndOfWord); 
}  

int main() 
{ 

    int t;
    int n , i, j;
    
    scanf("%d", &t);
    char A[100];

    for(i = 0; i < t; i++){

        scanf("%d", &n);

        char keys[n][100];


        char str[210], ch;

        int i, j, k;    

        scanf(" %c", &ch);

        i = 0;
        j = 0;
            
        while (ch != '\n')
        {   
            str[j] = ch;
            ch = getchar();
            j++;    
        }
        
        str[j] = '\0';

        scanf("%s", A);

        int sizeOfString = strlen(str);
        
        char *p;

        p = strtok (str," ");

        i = 0;

        while (p!= NULL)
        {
            //printf ("%s\n",p);
            strcpy(keys[i], p);
            p = strtok (NULL, " ");
            i++;
        }
       

    //Input keys (use only 'a' through 'z' and lower case) 
  
    //char output[][32] = {"Not present in trie", "Present in trie"}; 
  
  
    struct TrieNode *root = getNode(); 
  
    // Construct trie  
    for (i = 0; i < ARRAY_SIZE(keys); i++) 
        insert(root, keys[i]); 
  
    // Search for different keys 
    bool v = search(root, A);
    printf("%d\n", v);
    // printf("%s --- %s\n", "the", output[search(root, "the")] ); 
    // printf("%s --- %s\n", "these", output[search(root, "these")] ); 
    // printf("%s --- %s\n", "their", output[search(root, "their")] ); 
    // printf("%s --- %s\n", "thaw", output[search(root, "thaw")] ); 
    
    }   
  
    return 0; 
} 

