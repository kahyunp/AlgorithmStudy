#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
int main() {
	int c;
	scanf("%d", &c);
	char arr[50];
	scanf("%s", arr);
	long long result = 0;

    int i = c-1 ;

	while (i >= 0) {
		result = (result*31 + ((int)arr[i] - 96))%1234567891;
		i=i-1;
	}
	printf("%d", result);
}
