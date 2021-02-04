#include <iostream>
using namespace std;
int main() {
	int N, list[1000000] = {0}, low, high;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> list[i];
	}
	low = list[0];
	for (int i = 0; i < N; i++)
	{
		
		if (list[i] < low)
			low = list[i];
		else
			continue;
	}	
	high = list[0];
	for (int i = 0; i < N; i++)
	{	
	
		if (list[i] > high)
			high = list[i];
		else
			continue;
	}
	cout << low << " " << high;
	return 0;


}
