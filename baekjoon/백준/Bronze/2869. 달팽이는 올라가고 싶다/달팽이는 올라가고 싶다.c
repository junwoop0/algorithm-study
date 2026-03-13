#include <stdio.h>
#include <stdlib.h>

int main()
{
    int up, down;
    int total;
    int sum = 0;
    int count = 0;
    scanf("%d %d %d", &up, &down, &total);
    int sub = 0;
    sub = up - down;
    total -= up;
    count = total / sub;
    count ++;
    if ((total % sub) <= up && (total % sub) > 0)
        count++;
    printf("%d", count);
    return 0;
}