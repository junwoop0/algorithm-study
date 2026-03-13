#include <stdio.h>


int main()
{
    while (1)
    {
        int a, b = 0;
        int result = scanf("%d %d", &a, &b);
        if (result== EOF)
            break;
        printf("%d\n", a + b);
    }
    return 0;
}