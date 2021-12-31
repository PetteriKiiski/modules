#include <iostream>
#include "BinTree.h"
using namespace std;
int main()
{
	Element ele1 = 50;
	Element ele2 = 25;
	Element ele3 = 12;
	Element ele4 = 6;
	Element ele5 = 3;
	Element ele6 = 2;
	Element ele7(ele5, ele6, 1);
	Element element1(ele1, ele2);
	Element element2(ele3, ele4);
	cout << element1.value() << endl;
	cout << element2.value() << endl;
	cout << ele7.value() << endl;
	cout << element2.find(25) << endl;
	cout << element1.find(25) << endl;
	cout << ele1.hasright() << endl;
	cout << ele1.hasleft() << endl;
	cout << element1.hasright() << endl;
	cout << element1.hasleft() << endl;
	cout << element1.right().value() << endl;
	cout << element1.left().value() << endl;
	cout << ele7.find(25) << endl;
	return 0;
}
