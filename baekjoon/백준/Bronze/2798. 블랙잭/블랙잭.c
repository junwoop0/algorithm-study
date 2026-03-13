#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    int total;
    int *arr;
    int x = 0;
    int temp2 = 0;
    int temp1 = 0;
    scanf("%d %d", &n, &total);
    arr = (int *)malloc(sizeof(int) * n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (int i = 0; i < n-2; i++)
    {
        for (int j = i + 1; j < n-1; j++)
        {
            for (int k = j + 1; k < n; k++)
            {
                temp1 = arr[i] + arr[j] + arr[k];
                if ((temp1 > temp2) && temp1 <= total)
                {
                    temp2 = temp1;
                }
            }
        }
    }

    free(arr);

    printf("%d", temp2);
    return 0;
}