import Class
MyClass = Class.Class()
MyClass.create_private("TestVar", None)
MyClass.create_public("PublicVar", True)
MyClass.create_public_method("MyMethod", """return "for" """)
MyClass.create_public_method("PubMethod", """print("one-hundred dollars")
return self["MyMethod()"] + int(input())""")
print(MyClass["PubMethod()"])

