#include <iostream>
#include <string>
#include <sstream>
using namespace std;
int main() {
	//cs = converterstream
	stringstream cs;
	string s_a = "";
	string s_b = "";
	string s_c = "";
	int a = 0;
	int b = 0;
	int c = 0;
	cout << "Enter once side of the triangle" << endl;
	cin >> s_a;
	cout << "Enter another side of the triangle" << endl;
	cin >> s_b;
	cout << "Enter the last side of the triangle" << endl;
	cin >> s_c;
	cs << s_a;
	cs >> a;
	cs << s_b;
	cs >> b;
	cs << s_c;
	cs >> c;
	if (a + b != c || a + c != c || c + b != a) {
		cout << "This is not a triangle" << endl;
		return 0;
	}
	if (a * a + b * b == c * c) {
		cout << "This triangle is a right triangle" << endl;
	}
	else {
		cout << "This is not a right triangle" << endl;
	}
	return 0;
}
