#include <iostream>
#include <string>
using namespace std;

int main()
{
	double T,n;
	string answer;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> n;
		getline(cin, answer);
		for (int i = 0; i < answer.size(); i++)
		{
			switch (answer[i])
			{
			case '@':
				n *= 3;
				break;
			case '#':
				n -= 7;
				break;
			case '%':
				n += 5;
				break;
			}
		}
		printf("%.2f\n", n);
	}
	return 0;
}