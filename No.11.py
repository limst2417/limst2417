Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=int('1011',2)
>>> print(a)
11
>>> 
>>> a=int("1A"'16)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> a=int("1A",16)
...       
>>> print(a)
...       
26
