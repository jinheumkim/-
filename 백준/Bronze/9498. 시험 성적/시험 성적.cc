#include<stdio.h>

int main(void) {
    int N;
    scanf("%d", &N);
    if (90 <= N)  printf("A");
    else if (80 <= N) printf("B");
    else if (70 <= N) printf("C");
    else if (60 <= N) printf("D");
    else printf("F");

    return 0;
}