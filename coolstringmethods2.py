Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="happy birthday"
>>> x.index("birthday")
6
>>> x.find("birthday")
6
>>> y="00000000000happybirthday00000000"
>>> y.strip(0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    y.strip(0)
TypeError: strip arg must be None or str
>>> y.strip("0")
'happybirthday'
>>> y.rstrip("0")
'00000000000happybirthday'
>>> name=input("what is your name").strip()
what is your namey           u      s     ra
>>> print name
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(name)?
>>> print(name)
y           u      s     ra
>>> ".st
SyntaxError: EOL while scanning string literal
>>> len(name)
27
>>> 