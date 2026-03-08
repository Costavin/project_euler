#include <iostream>

#define MAX 4000000

int main() {
	long sum = 0;
	int a = 0;
	int b = 1;
	int next = 0;
	for (int i = 0; i < MAX; i++) {
		if (a > MAX)
			break;
		next = a+b;
		if (a%2==0)
			sum += a;
		a = b;
		b = next;
	}
	std::cout << sum << std::endl;
	return 0;
}
