#include <iostream>
#include <string>

using namespace std;

int main()
{
	while (1)
	{
		string s;
		getline(cin, s);

		if (s=="END")
		{
			break;
		}

		for (int i = (s.length() - 1); i >= 0; i--)
		{
			cout << s[i];
		}
		cout << '\n';
	}
	return 0;
}