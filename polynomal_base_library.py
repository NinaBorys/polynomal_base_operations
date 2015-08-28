#! /usr/bin/python3


class Polynom(object):

    def __init__(self, m=None, pol=None):
        if m:
            mod = (m + 1) * [0]
            mod[0] = 1
            mod[m] = 1
            mod[182] = 1
            self.m = m
            self.module = Polynom(pol=mod)
        self.array = pol and [int(x) for x in pol] or list()

    def const_zero(self):
        m = self.m
        res = (m + 1) * [0]
        return res

    def const_one(self):
        m = self.m
        res = (m + 1) * [1]
        return res

    def to_array(self, a_str):
        return [int(z) for z in a_str]

    def High_bit(self, a):
        for i, e in enumerate(a):
            if e == 1:
                return len(a[i:])
        return 0

    def __and__(self, value):
        return int(self) & value

    def __lshift__(self, value):
        temp = bin(int(self) << value)[2:]
        return 'm' in dir(self) and Polynom(self.m, temp) or Polynom(pol=temp)

    def __rshift__(self, value):
        temp = bin(int(self) >> value)[2:]
        temp = Polynom(self.m, temp)
        for e in range(len(self) - len(temp)):
            temp.insert(0, 0)
        return temp

    def insert(self, index, value):
        self.array.insert(index, value)

    def append(self, value):
        self.array.append(value)

    def __int__(self):
        return int(''.join(map(str, self)), 2)

    def __str__(self):
        for i, e in enumerate(self):
            if e:
                return ''.join(map(str, self.array[i:]))
        return '0'

    def __len__(self):
        return len(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __iter__(self):
        for x in self.array:
            yield x

    def __reversed__(self):
        for x in reversed(self.array):
            yield x

    def __add__(self, other):
        add_result = Polynom(self.m)

        if len(self) > len(other):
            for i in range(len(self) - len(other)):
                other.insert(0, 0)

        if len(other) > len(self):
            for i in range(len(other) - len(self)):
                self.insert(0, 0)

        for i, e in enumerate(self):
            x = e != other[i] and 1 or 0
            add_result.insert(i, x)
        return add_result

    def contains_single(self, element):
        if len(self) == 1 and element in self:
            return True
        return False

    def reduction(self):
        def first_is_bigger(first, second):
            return int(first) > int(second) and True or False

        r = Polynom(self.m, '0')
        q = Polynom(self.m, '0')

        t = self.High_bit(self.module)
        if self.module.contains_single(1):
            return r
        while (first_is_bigger(self, self.module)):

            k = self.High_bit(self)
            c = self.module
            c = c << k - t

            while (first_is_bigger(c, self) and (k - 1 - t) >= 0):
                k -= 1
                c = c >> 1

            temp = Polynom(self.m, '1')
            temp = temp << k - t
            q = q + temp
            self = self + c
        r = self
        for i, e in enumerate(r):
            if e:
                return Polynom(self.m, r[i:])
        return r

    def mul_on_number(self, n):
        result = Polynom(self.m)
        for e in self:
            result.append(e & n)
        return result

    def __mul__(self, other):
        mul_result = Polynom(self.m, '0')
        temp = Polynom(self.m)

        for e in reversed(other):
            temp.append(self.mul_on_number(e))

        for i, e in enumerate(temp):
            mul_result = mul_result + e << i
        return mul_result.reduction()

    def square(self):
        temp = Polynom(self.m)
        for e in range(len(self) * 2):
            if e % 2 == 0 and e != len(self) * 2 - 1:
                temp.append(0)
            else:
                temp.append(self[(e - 1) // 2])
        return temp.reduction()

    def __pow__(self, n):
        result = Polynom(self.m, '1')
        while int(n):
            if n & 1:
                result = result * self
                n = n + Polynom(self.m, '1')
            else:
                self = self.square()
                n = n >> 1
        return result

    def __invert__(self):
        result = self
        temp = self

        for i in range(1, self.m - 1):
            temp = temp.square()
            result = temp * result
        return result.square()

    def Trace(self):
        trace = self
        temp = self

        for i in range(1, self.m):
            temp = temp.square()
            trace = trace + temp

        for i, e in enumerate(trace):
            if e:
                return Polynom(self.m, trace[i:])
