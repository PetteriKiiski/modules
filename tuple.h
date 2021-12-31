#include <deque>
template <>
class Tuple
{
private:
	template <typename type>
	class Item
	{
	private:
		type value;
	public:
		Item(){};
		Item(const Item& copysource)
		{
			value = copysource.value;
		}
		Item(int Value) : value(Value) {};
		Item& operator= (const Item& copysource)
		{
			value = copysource.value;
			return *this;
		}
		void operator= (type TheValue)
		{
			value = TheValue;
		}
		operator type()
		{
			return value;
		}
	}
	deque<Item>;
public:
	Tuple()
}
