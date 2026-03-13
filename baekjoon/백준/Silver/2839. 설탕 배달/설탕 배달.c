#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int size;
    scanf("%d", &size);
    int num5 = 0;
    int num3 = 0;
    int sum = 0;
    while (size > 0)
    {
        if (size == 12)
        {
            num3 += 4;
            size = 0;
            break;
        }
        if (size == 9)
        {
            num3 += 3;
            size = 0;
            break;
        }
        if (size == 6)
        {
            num3 += 2;
            size = 0;
            break;
        }
        if (size == 3)
        {
            num3++;
            size = 0;
            break;
        }
        size -= 5;
        num5++;
    }
    sum = num3 + num5;
    if (size != 0)
        sum = -1;
    printf("%d", sum);
    return 0;
}