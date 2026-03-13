#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    int x = 1;
    int max, min;
    while ((x <= a) && (x <= b))
    {
        if ((a % x == 0) && (b % x == 0))
        {
            max = x;
        }
        x++;
    }
    min = a * b / max;
    printf("%d\n", max);
    printf("%d", min);
    return 0;
}