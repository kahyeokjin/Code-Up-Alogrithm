#include <iostream>
using namespace std;
int main()
{
	int T;

	cin >> T;

	while(T--)
	{
		int n;
		int arr[20];
		int sum = 0;
		int space;
		int MIN = 100, MAX = 0;
		cin >> n;
		for (int j = 0; j < n; j++)
		{
			cin >> arr[j];
			sum += arr[j];
			if (MIN > arr[j]) MIN = arr[j];
			if (MAX < arr[j]) MAX = arr[j];
		}
		space = sum / n;

		int result = 2 * (MAX - space) + 2 * (space - MIN);

		cout << result << "\n";


	}
	
	return 0;

}