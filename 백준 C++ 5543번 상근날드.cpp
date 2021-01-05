#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
	vector <int>bur(3);
	vector <int>drink(2);
	for (int i = 0; i < 3; i++)
	{
		cin >> bur[i];
	}
	sort(bur.begin(), bur.end());
	
	for (int i = 0; i < 2; i++)
	{
		cin >> drink[i];
	}
	sort(drink.begin(), drink.end());
	int result = bur[0] + drink[0]-50;
	cout << result;
	return 0;

}