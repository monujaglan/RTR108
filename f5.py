Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> a
5
>>> 
========================= RESTART: /home/user/f5.py =========================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/f5.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/f5.py', 'a': 10}
>>> type(a)
<class 'int'>
>>> type(b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(b)
NameError: name 'b' is not defined
>>> type(c)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(c)
NameError: name 'c' is not defined
>>> 
========================= RESTART: /home/user/f5.py =========================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/f5.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/f5.py', 'a': 10, 'b': 1.1, 'c': 'd'}
>>> type(b)
<class 'float'>
>>> type(c)
<class 'str'>
>>> type(a)
<class 'int'>
>>> PRINT(4)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    PRINT(4)
NameError: name 'PRINT' is not defined
>>> print(4)
4
>>> ## pracrtice P4YE
>>> type('Hello World!)
	 
SyntaxError: EOL while scanning string literal
>>> type('Hello World')
	 
<class 'str'>
>>> type(17)
	 
<class 'int'>
>>> type(3.2)
	 
<class 'float'>
>>> type(17)
	 
<class 'int'>
>>> type('3.2')
	 
<class 'str'>
>>> print(1,000,000)
	 
1 0 0
>>> 1
	 
1
>>> 1+1
	 
2
>>> x=5
	 
>>> x+1
	 
6
>>> 
