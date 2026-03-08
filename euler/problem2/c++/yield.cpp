#include <iostream>
#include <generator>

#define MAX 4000000

std::generator<int> genFibo() {
	int a = 0;
	int b = 1;
	int next = 0;
	while(true)	{
		co_yield a;
		next = a+b;
		a = b;
		b = next;
	}
}

int main() {
	int even_acc = 0;
	for (int val : genFibo()) {
		if (val > MAX)
			break;
		if (val%2 == 0)
			even_acc = even_acc + val;
	}
	std::cout << even_acc << std::endl;
	return 0;
}

#g++ -std=c++23 yield.cpp
