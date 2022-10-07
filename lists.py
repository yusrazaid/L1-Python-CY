Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> our_list=[27,46,-5,17,99]
>>> print(our_list)
[27, 46, -5, 17, 99]
>>> type(our_list)
<class 'list'>
>>> jackson=["A","B","C",1,2,3,"DO","REY","MI",True,False]
>>> jackson[4]
2
>>> jackson[7]
'REY'
>>> jackson[-2]
True
>>> x=jackson[6]
>>> x
'DO'
>>> jackson[0:3]
['A', 'B', 'C']
>>> jackson
['A', 'B', 'C', 1, 2, 3, 'DO', 'REY', 'MI', True, False]
>>> our_list=[1,2,[3,4,5],6,7,8]
>>> our_list[2]
[3, 4, 5]
>>> our_table=[  [1,2,3] , [4,5,6] , [7,8,9] ]
>>> our_table[1]
[4, 5, 6]
>>> our_table[2]
[7, 8, 9]
>>> our_table[0][2]
3
>>> our_table[2][1]
8
>>> our_table[1][3]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    our_table[1][3]
IndexError: list index out of range
>>> our_table[1][2]
6
>>> our_table[1][1:]
[5, 6]
>>> 