import ctypes
import os
_file = "test.c"
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file,)))
_mod = ctypes.cdll.LoadLibrary(_path)
_mod.execute()
