Polynomial base operations

Small library for perfoming arithmetic operations with polynoms

Added:
- '__add__'
- '__mul__'
- 'sqare'
- '__pow__'
- 'inverse_element'
- 'Trace'

Example:
```python
s1 = '1011100110111111'
s2 = '100100110101011001'
m = 191
x = Polynom(m, s1)
y = Polynom(m, s2)
z = x + y
print(z)

>>> 101111010011100110
```