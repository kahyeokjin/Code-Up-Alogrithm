#include <iostream>
#include <algorithm>

using namespace std;
int main()
{
	int T, score[5], sum = 0,fin;
	cin >> T;
	int* result = new int[T];
	
	for (int i = 0; i < T; i++)
	{
		for (int a = 0; a < 5; a++)
		{
			cin >> score[a];
		}
		sort(score, score + 5);

		if (score[3] - score[1] >= 4)
		{
			result[i] = -1;
		}
		else
		{
			result[i] = score[1] + score[2] + score[3];
		}
	}
	for(int i=0; i<T; i++)
	{
		if (result[i] == -1)
		{
			cout << "KIN" << endl;
		}
		else
		{
			cout << result[i] << endl;
		}
	}
	return 0;
		
	
}