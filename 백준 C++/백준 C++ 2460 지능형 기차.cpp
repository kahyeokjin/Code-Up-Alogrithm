#include <iostream>
using namespace std;
int main()
{
	int total = 0, big = 0, in, out;
	for (int i = 0; i < 10; ++i)
	{
		cin >> out >> in;
		total = total + in - out;
		
		if (total > big)
			big = total;
	}
	cout << big;
	
	return 0;
}
