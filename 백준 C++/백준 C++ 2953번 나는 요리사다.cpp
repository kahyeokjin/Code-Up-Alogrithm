#include <iostream>
using namespace std;

int main()
{
	int cook[5][5];
	int  win=0,winsum=0;
	
	for (int i = 0; i < 5; i++)
	{
		int sum = 0;
		for (int j = 0; j < 4; j++)
		{
			cin >> cook[i][j];
			sum = sum + cook[i][j];
		}
		cook[i][4] = sum;
		if (cook[i][4] > cook[win][4])
		{
			win = i;
		}
	}
	cout << win+1 << " " << cook[win][4];
	return 0;
}
