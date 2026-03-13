#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int find;
    int count = 1;
    int i = 0;
    scanf("%d", &find);
    while (find > 0)
    {
        find -= i;
        if (find <= 1)
            break;
        count++;
        i += 6;
    }
    printf("%d", count);
    return 0;
}