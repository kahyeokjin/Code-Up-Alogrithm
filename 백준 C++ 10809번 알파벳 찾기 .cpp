#include <iostream>
#include <string>

using namespace std;

int main()
{
	string line;
	string alp = "abcdefghijklmnopqrstuvwxyz";
	cin >> line;
	for (int i = 0; i < alp.size(); i++)
	{
		cout << (int)line.find(alp[i])<< " ";
	}
	return 0;
}