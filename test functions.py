Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> letter = 'fruit[1]
SyntaxError: EOL while scanning string literal
>>> x = x+1
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x = x+1
NameError: name 'x' is not defined
>>> x = 0
>>> x = x + 1
>>> type(32)
<class 'int'>
>>> max('Hello world')
'w'
>>> min('hello world')
' '
>>> len('Hello world')
11
>>> 
>>> int('32')
32
>>> int('Hello')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int('Hello')
ValueError: invalid literal for int() with base 10: 'Hello'
>>> int(4.555)
4
>>> int(-3.4)
-3
>>> float(33)
33.0
>>> float('3.14159')
3.14159
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
>>> import math
>>> print(math)
<module 'math' (built-in)>
>>> ratio = signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> signal_power
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    signal_power
NameError: name 'signal_power' is not defined
>>> ratio = sin_x / cox_x
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ratio = sin_x / cox_x
NameError: name 'sin_x' is not defined
>>> ratio = 4 / 2
>>> decibels = 10 * math.log10
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    decibels = 10 * math.log10
TypeError: unsupported operand type(s) for *: 'int' and 'builtin_function_or_method'
>>> decibels = 10 * log10
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    decibels = 10 * log10
NameError: name 'log10' is not defined
>>> degrees = 45
>>> radians = degrees / 360.0 * 2 * math.pi
>>> math.sin(radians)
0.7071067811865475
>>> math.sqrt(2) / 2.0
0.7071067811865476
>>> import random
>>> for i in range (10)
SyntaxError: invalid syntax
>>> for i in range(10):
	x = random.random()
	print(x)

	
0.7492854997487792
0.34504173170929564
0.7349703076309466
0.3373242273721039
0.36879221122635675
0.9413369205103492
0.02524547385186038
0.5407561265560509
0.933457004330358
0.13074893254571462
>>> random.randiant(5,10)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    random.randiant(5,10)
AttributeError: module 'random' has no attribute 'randiant'
>>> (5, 10)
(5, 10)
>>> (5, 10)
(5, 10)
>>> t = [1, 2, 3]
>>> random.choice(t)
1
>>> random.choice(t)
2
>>> 
