#include <stdio.h>
#include <stdlib.h>

int main()
{
    int H, W, N, M, a, b;
    scanf("%d %d %d %d", &H, &W, &N, &M);
    N++;
    M++;
    a = H / N;
    b = W / M;
    if (H % N != 0) a++;
    if (W % M != 0) b++; //올림
    printf("%d", a*b);
    return 0;
}