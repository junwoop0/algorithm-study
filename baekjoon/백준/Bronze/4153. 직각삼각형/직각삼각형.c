#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int a, b, c;
    while (1)
    {
        scanf("%d %d %d", &a, &b, &c);
        if (a == 0)
            break;
        a = a * a;
        b = b * b;
        c = c * c;
        if ((a + b == c) || (a + c == b) || (b + c == a))
        {
            printf("right\n");
        }
        else
            printf("wrong\n");
    }
    return 0;
}