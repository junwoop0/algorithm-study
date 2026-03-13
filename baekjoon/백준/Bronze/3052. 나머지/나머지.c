#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int arr[10] = {0};
    int count = 10;
    int isunique = 0;
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", arr + i);
    }
    for (int i = 0; i < 10; i++)
    {
        arr[i] = arr[i] % 42;
        isunique = 0;
        for (int j = 0; j < i; j++)
        {
            if (arr[j] == arr[i])
                isunique = 1;
        }
        if (isunique == 1)
            count--;
    }
    printf("%d", count);
    return 0;
}