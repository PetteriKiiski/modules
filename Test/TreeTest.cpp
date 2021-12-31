#include </home/sepatuu/peter/module/BinTree.h>
#include <iostream>
using namespace std;
bool in(int element, BinaryItem node)
{
	if (element == int(node))
	{
		return true;
	}
	if (element > int(node))
	{
		if (node.has_right())
		{
			return in(element, *(node.right()));
		}
		else
		{
			return false;
		}
	}
	else
	{
		if (node.has_left())
		{
			return in(element, *(node.left()));
		}
		else
		{
			return false;
		}
	}
	return true;
}
int main()
{
	BinaryItem Node;
	int item = 0;
	cout << "Enter an int: ";
	cin >> item;
	Node.AddItem(BinaryItem(item));
	cout << "Enter an int: ";
	cin >> item;
	Node.AddItem(BinaryItem(item));
	cout << "Enter an int: ";
	cin >> item;
	Node.AddItem(BinaryItem(item));
	cout << "Enter an int: ";
	cin >> item;
	Node.AddItem(BinaryItem(item));
	cout << "Enter an int: ";
	cin >> item;
	Node.AddItem(BinaryItem(item));
	cout << "Enter an int: ";
	cin >> item;
	Node.AddItem(BinaryItem(item));
	cout << "Enter an int: ";
	cin >> item;
	Node.AddItem(BinaryItem(item));
	cout << "What item do you wish to find?: ";
	cin >> item;
	if (in(item, Node))
	{
		cout << "The item you wished to find is in your inputs" << endl;
	}
	else
	{
		cout << "Not in your inputs\n";
	}
	return 0;
}
