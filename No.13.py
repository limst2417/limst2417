Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> int('1002',2)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int('1002',2)
ValueError: invalid literal for int() with base 2: '1002'
>>> 
>>> int('1008',8)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int('1008',8)
ValueError: invalid literal for int() with base 8: '1008'
>>> 
>>> 
>>> int('AAFG',16)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int('AAFG',16)
ValueError: invalid literal for int() with base 16: 'AAFG'
