#include <iostream>
#include "StringVector.cpp"
using namespace std;
void DisplayVector(Vector<int> Copy)
{
	cout << "Displaying Array" << endl;
	for (int x = 0; x < Copy.len(); x += 1)
	{
		cout << Copy[x] << endl;
	}
}
int main()
{
	cout << "Vector object: vector(3)" << endl;
	Vector<int> vector (3);
	DisplayVector(vector);
	cout << "Enter first integer: ";
	int object = 0;
	cin >> object;
	vector.ChangeVal(object, 0);
	DisplayVector(vector);
	cout << "Enter second integer: ";
	cin >> object;
	vector.ChangeVal(object, 1);
	DisplayVector(vector);
	cout << "Enter last integer: ";
	cin >> object;
	vector.ChangeVal(object, 2);
	DisplayVector(vector);
	cout << "Enter pushback: ";
	cin >> object;
	vector.PushBack(object);
	DisplayVector(vector);
	return 0;
}
