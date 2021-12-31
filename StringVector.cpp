namespace module {
template <typename type>
class Vector
{
private:
	int ArrayLength = 5;
	int* MyVector = nullptr;
	int* TestVector = nullptr;
	int* NewVector = nullptr;
public:
	Vector() {};
	Vector(int arrlength) : ArrayLength(arrlength)
	{
		NewVector = new int[ArrayLength + 1];
		TestVector = new int[ArrayLength];
		MyVector = new int[ArrayLength];
		if (arrlength > ArrayLength)
		{
			for (int x = 0; x < arrlength - 5; x += 1)
			{
				PushBack(0);
			}
		}
		else if (arrlength < ArrayLength)
		{
			for (int x = 0; x > arrlength - 5; x -= 1)
			{
				PopOff();
			}
		}
	}
	~Vector()
	{
		delete[] MyVector;
		delete[] TestVector;
		delete[] NewVector;
	}
	void PushBack(type add)
	{
		for (int x = 0; x < ArrayLength; x += 1)
		{
			NewVector[x] = MyVector[x];
		}
		NewVector[ArrayLength + 1] = add;
		delete[] MyVector;
		MyVector = new int[ArrayLength + 1];
		for (int x = 0; x < ArrayLength + 1; x += 1)
		{
			MyVector[x] = NewVector[x];
		}
		MyVector[ArrayLength + 1] = NewVector[ArrayLength + 1];
		delete[] NewVector;
		NewVector = nullptr;
		++ArrayLength;
	}
	void PopOff()
	{
		NewVector = new int[ArrayLength - 1];
		for (int x = 0; x < ArrayLength - 1; x += 1)
		{
			NewVector[x] = MyVector[x];
		}
		delete[] MyVector;
		MyVector = new int[ArrayLength - 1];
		for (int x = 0; x < ArrayLength - 1; x += 1)
		{
			MyVector[x] = NewVector[x];
		}
		delete[] NewVector;
		NewVector = nullptr;
		--ArrayLength;
	}
	int len()
	{
		return ArrayLength;
	}
	operator type*()
	{
		return MyVector;
	}
	type operator[](int num)
	{
		if (num <= len() - 1 && num >= 0)
			return MyVector[num];
		else
			return 0;
	}

	void operator=(Vector<type> Copy)
	{
		if (Copy.len() <= len());
		{
			for(int x = 0; x < Copy.len(); x += 1)
			{
				Copy.MyVector[x] = MyVector[x];
			}
		}
		if (Copy.len() >= len());
		{
			for(int x = 0; x < len(); x += 1)
			{
				Copy.MyVector[x] = MyVector[x];
			}
		}
	}
	int operator+(Vector<type> Copy)
	{
		NewVector = new int[ArrayLength + Copy.len()];
		TestVector = MyVector;
		for (int x = len(); x < len() + Copy.len(); ++x)
		{
			TestVector[x] = Copy[x];
		}
		return TestVector;
	}
	void operator+=(Vector<type> BCopy)
	{
		MyVector = MyVector + BCopy;
	}
};
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
}
