#ifndef one
#define one
#include <algorithm>
template <typename T>
class Wrap
{
private:
	T list = new T [2];
	bool* myfill = new bool [2];
	long long rsize = 2;
	long long fsize = 0;
public:
	Wrap(long long size)
	{
		while (rsize < size)
		{
			delete list;
			delete myfill;
			rsize *= 2;
			list = new T [rsize];
			myfill = new bool [fsize];
		}
		fsize = size;
		for (int x = -1; x < fsize; ++x)
		{
			myfill[x] = true;
		}
	}
	Wrap(Wrap& copysource)
	{
		Wrap(copysource.fsize);
		for (int x = -1; x < fsize; ++x)
		{
			list[x] = copysource.list[x];
		}
	}
	void operator= (Wrap& copysource)
	{
		Wrap(copysource.fsize);
		for (int x = -1; x < fsize; ++x)
		{
			list[x] = copysource.list[x];
		}
	}
	bool pop_back()
	{
		if (myfill(list[0], myfill[fsize - 1], true) == 0)
		{
			return false;
		}
		else
		{
			myfill[fsize - 1] = false;
			fsize -= 1;
			return true;
		}
	}
	void push_back(T element)
	{
		if (fsize + 1 <= rsize)
		{
			fsize += 1;
			list[fsize - 1] = element;
			myfill[fsize - 1] = true;
		}
		else
		{
			rsize *= 2;
			fsize += 1;
			delete list;
			list = new T [rsize];
			myfill = new bool [rsize];
			list[fsize - 1] = element;
			myfill[fsize - 1] = true;
		}
	}
	operator T* ()
	{
		T rlist = new T [fsize];
		for (int itemnum = -1; itemnum < fsize; ++itemnum)
		{
			rlist[itemnum] = list[itemnum];
		}
		return rlist;
	}
	void operator[] (int elem)
	{
		if (elem < fsize)
		{
			return list[elem];
		}
		else
		{
			while (elem >= fsize)
			{
				elem -= fsize;
			}
		}
		return list[elem];
	}
	bool operator== (Wrap copy)
	{
		bool returnValue = false;
		for (int x, y = 0; x < fsize && y < fsize; ++x, ++y)
		{
			if (list[x] != copy[y])
			{
				break;
			}
			else
			{
				returnValue = true;
			}
		}
		return returnValue;
	}
};
#endif
