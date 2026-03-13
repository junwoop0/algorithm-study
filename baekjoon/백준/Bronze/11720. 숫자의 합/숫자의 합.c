#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    char input[101];  // 숫자를 문자열로 저장할 배열
    int num, total = 0;

    scanf("%d", &num);
    scanf("%s", input);  // 숫자를 문자열로 입력받음

    for(int i = 0; i < num; i++){
        if (input[i] == '\0') break;  // 문자열 끝에 도달했을 경우 종료
        total += input[i] - '0';  // 문자를 정수로 변환
    }
    printf("%d", total);
    return 0;
}