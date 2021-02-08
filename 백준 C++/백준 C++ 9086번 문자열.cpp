#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int a=0; a < T; a++)
	{
		string str;
		cin >> str;
		int siz = str.size();
		cout << str[0] << str[siz-1] << endl;
	}
	return 0;
}