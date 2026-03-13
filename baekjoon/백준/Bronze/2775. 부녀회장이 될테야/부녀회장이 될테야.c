#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int recursive(int a, int b)
{
    int num = 0;
    if (a == 0)
        return b;
    else
    {
        for (int i = 0; i <= b; i++)
        {
            num += recursive(a - 1, i);
        }
        return num;
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    int a, b;
    for (int i = 0; i < n; i++)
    {
        int sum = 0;
        scanf("%d", &a);
        scanf("%d", &b);
        sum = recursive(a, b);
        printf("%d\n", sum);
    }
    return 0;
}