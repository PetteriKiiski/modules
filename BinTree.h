class InvalidTreeError{};
class Element
{
private:
	Element* rightptr = nullptr;
	Element* leftptr = nullptr;
	int integer = -1;
public:
	Element(){};
	Element(Element ele1, Element ele2, int val)
	{
		if (ele1.value() > ele2.value())
		{
			*rightptr = ele1;
			*leftptr = ele2;
		}
		else if (ele2.value() > ele1.value())
		{
			*rightptr = ele2;
			*leftptr = ele1;
		}
		else
		{
			throw InvalidTreeError();
		}
		integer = val;
	}
	Element(int val)
	{
		integer = val;
	}
	Element(Element right, Element left)
	{
		*rightptr = right;
		*leftptr = left;
	}
	Element(const Element &element)
	{
		if (element.hasleft())
		{
			Element* leftptr = *(element.leftptr)
		}
		else
		{
			Element* leftptr = nullptr;
		}
		if (element.hasright())
		{
			Element* rightptr = *(element.rightptr)
		}
		else
		{
			Element* rightptr = nullptr;
		}
		integer = element.integer
	}
	Element right()
	{
		return *rightptr;
	}
	Element left()
	{
		return *rightptr;
	}
	int value()
	{
		return integer;
	}
	void setright(Element ele)
	{
		if (ele.value() > leftptr->value())
		{
			*rightptr = ele;
		}
		else
		{
			throw InvalidTreeError();
		}
	}
	void setleft(Element ele)
	{
		if (ele.value() < leftptr->value())
		{
			*leftptr = ele;
		}
		else
		{
			throw InvalidTreeError();
		}
	}
	void Reset()
	{
		Element* rightptr = nullptr;
		Element* leftptr = nullptr;
		int integer = -1;
	}
	void Reset(Element ele1, Element ele2, int val)
	{
		if (ele1.value() > ele2.value())
		{
			*rightptr = ele1;
			*leftptr = ele2;
		}
		else if (ele2.value() > ele1.value())
		{
			*rightptr = ele2;
			*leftptr = ele1;
		}
		else
		{
			throw InvalidTreeError();
		}
		integer = val;
	}
	bool hasright()
	{
		if (*rightptr == nullptr)
		{
			return false;
		}
		return true;
	}
	bool hasleft()
	{
		if (*leftptr == nullptr)
		{
			return false;
		}
		return true;
	}
	void Reset(int val)
	{
		Element* rightptr = nullptr;
		Element* leftptr = nullptr;
		integer = val;
	}
	void Reset(Element right, Element left)
	{
		Element* rightptr = right;
		Element* leftptr = left;
		integer = -1;
	}
	bool find(int val)
	{
		if (val == value())
		{
			return true;
		}
		if (val > value())
		{
			if (! hasright())
			{
				return false;
			}
			return rightptr->find(val);
		}
		if (val < value())
		{
			if (! hasleft())
			{
				return false;
			}
			return leftptr->find(val);
		}
		return false;
	}
	bool operator== (std::nullptr_t null)
	{
		return false;
	}
	const Element operator= (const Element &element)
	{
		if (element.hasleft())
		{
			Element* leftptr = *(element.leftptr)
		}
		else
		{
			Element* leftptr = nullptr;
		}
		if (element.hasright())
		{
			Element* rightptr = *(element.rightptr)
		}
		else
		{
			Element* rightptr = nullptr;
		}
		integer = element.integer
		return *this
	}
};
