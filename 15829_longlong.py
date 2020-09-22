#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
#define M 1234567891
int main() {
	long long c;
	scanf("%d", &c);
	char arr[50];
	scanf("%s", arr);
	long long result = 0;
	long long tmp = 1;

	for (int i = 0; i < c; i++) {
		result =( result + (((int)arr[i] - 96) * tmp))%M;
		tmp = tmp * 31;
		tmp=tmp% M;
	}
	printf("%d", result%M);
}
