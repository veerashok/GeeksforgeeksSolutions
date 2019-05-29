#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
int compare(char str1[100], char str2[100]){

    int length1 = strlen(str1);
    int length2 = strlen(str2);
    int count = 0;

    if(length2 > length1){
        count = length1;
    }
    else{
        count = length2;
    }


    for (int i = 0; i < count; ++i)
    {
        if( str1[i] > str2[i] ){
            return 0;
        }
        else if( str1[i] == str2[i] ){
            i++;
        }
        else{
            return 1;
        }
    }

    return 0;


}
void sorting(char arr[50][50], int n){
    int i = 0, j = 0, index;
    char min[50];

    while(i < n){
        j = i;
        index = i;
        strcpy(min, arr[j]);

        while(j < n){
            //printf("%d", compare(min, arr[j]));
            if(compare(min, arr[j])){
                strcpy(min, arr[j]);
                index = j; 

            }

            j++;
        }

        strcpy(arr[index], arr[i]);
        //arr[index] = arr[i];
        strcpy(arr[i], min);
        printf("%s\n", min); //arr[i] = min; 
        i++;
    } 

    for (i = 0; i < n; ++i)
    {
        printf("%s\n", arr[i]);
        
    }

    return;

}
int main()
{
    char str1[100];
    char newString[50][50]; 
    int i,j,ctr;   
 
    fgets(str1, sizeof str1, stdin);    
 
    j=0; ctr=0;
    for(i=0;i<=(strlen(str1));i++)
    {
        // if space or NULL found, assign NULL into newString[ctr]
        if(str1[i]==' '||str1[i]=='\0')
        {
            newString[ctr][j]='\0';
            ctr++;  //for next word
            j=0;    //for next word, init index to 0
        }
        else
        {
            newString[ctr][j]=str1[i];
            j++;
        }
    }
    //printf("\n Strings or words after split by space are :\n");
    for(i=0;i < ctr;i++)
        printf("%s\n",newString[i]);

    sorting(newString, ctr);
    return 0;
}