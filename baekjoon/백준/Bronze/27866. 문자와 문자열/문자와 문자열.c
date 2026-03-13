#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char arr[1001] = {0};
    int i;
    scanf("%s", arr);
    scanf("%d", &i);
    printf("%c", arr[i-1]);
    return 0;

}