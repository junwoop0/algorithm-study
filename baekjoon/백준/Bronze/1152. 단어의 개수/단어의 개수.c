#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

    char arr[1000001] = {0};
    gets(arr);
    int count = 0;
    for (int i = 0; i < sizeof(arr); i++)
    {
        if (arr[i] != ' ' && arr[i + 1] == ' ')
        {
            count++;
        }
        else if (arr[i] == ' ' && arr[i + 1] == '\0')
            count--;
        else if (arr[i] == '\0')
        {
            count++;
            break;
        }
    }
    printf("%d", count);
    return 0;
}