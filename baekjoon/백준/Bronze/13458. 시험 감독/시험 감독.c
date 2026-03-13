#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n;
    int *arr;
    int b, c;
    long long total = 0;
    scanf("%d", &n);
    arr = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    scanf("%d %d", &b, &c);
    total += n;
    for (int i = 0; i < n; i++)
    {
        arr[i] -= b;
        if (arr[i] < 0)
            continue;
        total += arr[i] / c;
        if ((arr[i] % c) != 0)
            total++;
    }
    printf("%ld", total);
    free(arr);
    return 0;
}