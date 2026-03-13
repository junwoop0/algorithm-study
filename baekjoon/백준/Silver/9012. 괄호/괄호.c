#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n;
    int left = 0;
    int right = 0;
    char arr[51];
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        left = 0;
        right = 0;
        scanf("%s", arr);
        int j = 0;
        while (arr[j] != '\0')
        {
            if (arr[j] == '(')
            {
                left++;
            }
            else if (arr[j] = ')')
            {
                right++;
            }
            j++;
            if (right > left)
                break;
        }
        if (left == right)
        {
            printf("YES\n");
        }
        else
            printf("NO\n");
    }
    return 0;
}