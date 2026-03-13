#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n;
    char arr[80] = {0};
    int total = 0;
    int sum = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        total = 0;
        memset(arr, 0, sizeof(arr));
        scanf("%s", arr);
        int j = 0;
        while (arr[j] != '\0')
        {
            if (arr[j] == 'O' && arr[j - 1] == 'O')
            {
                sum++;
                total += sum;
            }
            else if (arr[j] == 'X')
                sum = 1;
            else

            {
                sum = 1;
                total += sum;
            }
            j++;
        }
        printf("%d\n", total);
    }
    return 0;
}