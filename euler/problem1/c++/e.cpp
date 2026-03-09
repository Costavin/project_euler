#include <iostream>
#include <chrono>

int limit = 999;

int gauss_sum(int x) {
	int p = limit/x;
	return x*(p*(p+1))/2;
}

int main() {
	int result = 0;
	
	auto start = std::chrono::high_resolution_clock::now();
	for (int i = 0; i < limit+1; i++)
		if ((i%3==0) || (i%5==0))
			result = result + i;
	
	auto end = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);

	std::cout << "Result: " << result << "\nfor cicle"<< std::endl;
	std::cout << "Elapsed time: " << duration.count() << " nanoseconds" << std::endl;


	start = std::chrono::high_resolution_clock::now();
	
	result = gauss_sum(3) + gauss_sum(5) - gauss_sum(15);

	end = std::chrono::high_resolution_clock::now();
	duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);


	std::cout << "Result: " << result << "\nGauss formula" << std::endl;
    	std::cout << "Elapsed time: " << duration.count() << " nanoseconds" << std::endl;

	return 0;
}
