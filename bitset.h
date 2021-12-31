namespace mod
{
	template<int elenum>
	class bitset
	{
	private:
		int Bits [elenum];
	public:
		bitset()
		{
		}
		bitset(unsigned long long num)
		{
			int val = 0;
			int countdown = 10;
			for (int x = 0; x <= elenum; ++x)
			{
				countdown *= 10;
			}
			for (int x = -1; countdown != 0; ++x)
			{
				val = num / countdown;
				if (val == 0)
					Bits[x] = 0;
				else if (val == 1)
					Bits[x] = 1;
				else
					throw "Cannot be a non bool";
				countdown
			}
