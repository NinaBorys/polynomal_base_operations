#! /usr/bin/python3.3


class Polynom(object):

    def __init__(self, modul, m):
        self.modul = modul
        self.m = m
        pass

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

    def to_string(self, a_arr):
        k = ''.join([str(e) for e in a_arrr])
        return k

    def High_bit(self, a):
        res = 0
        for i in range(0, len(a), 1):
            if a[i] == 1:
                res = len(a[i:])
                break
        return res

    def bit_and(self, a):
        temp = int(''.join([str(e) for e in a]), 2)
        return temp & 1

    def shift_left(self, a, k):
        temp = bin(int(''.join([str(e) for e in a]), 2) << k)[2:]
        return list([int(c) for c in temp])

    def shift_right(self, a, k):
        len1 = len(a)
        temp = bin(int(''.join([str(e) for e in a]), 2) >> k)[2:]
        len2 = len(temp)
        res = list([int(c) for c in temp])

        for i in range(0, len1 - len2, 1):
            res.insert(0, 0)
        return res

    def first_is_bigger(self, first, second):
        a = int(''.join([str(e) for e in first]), 2)
        b = int(''.join([str(e) for e in second]), 2)

        if a > b:
            return True
        else:
            return False

    def addition(self, first, second):
        add_result = []

        if len(first) > len(second):
            for i in range(0, len(first) - len(second), 1):
                second.insert(0, 0)

        if len(second) > len(first):
            for i in range(0, len(second) - len(first), 1):
                first.insert(0, 0)

        for i in range(0, len(first), 1):
            if(first[i] == second[i]):
                add_result.insert(i, 0)
            else:
                add_result.insert(i, 1)
        return add_result

    def reduction(self, a, mod):
        r = [0]
        q = [0]

        t = self.High_bit(mod)

        if mod == [1]:
        	return r

        while (self.first_is_bigger(a, mod)):

            k = self.High_bit(a)
            c = mod
            c = self.shift_left(c, k - t)

            while (self.first_is_bigger(c, a) and (k - 1 - t) >= 0):
                k -= 1
                c = self.shift_right(c, 1)

            temp = [1]
            temp = self.shift_left(temp, (k - t))
            q = self.addition(q, temp)
            a = self.addition(a, c)
        r = a
        for i in range(0, len(r)):
            if r[i] != 0:
                r = r[i:]
                break
        return r

    def mul_on_number(self, arr, n):
        result = []
        for i in range(0, len(arr), 1):
            result.insert(i, arr[i] & n)
        return result

    def multiplication(self, a, b):
        mul_result = [0]
        temp = []

        for i in range(len(b) - 1, -1, -1):
            temp.append(self.mul_on_number(a, b[i]))

        for i in range(0, len(temp), 1):
            temp[i] = self.shift_left(temp[i], i)

        for i in range(0, len(temp)):
            mul_result = self.addition(mul_result, temp[i])

        mul_result = self.reduction(mul_result, self.modul)
        return mul_result

    def square(self, a):
        result = []
        temp = [0 if e % 2 == 0 and e != len(
            a) * 2 - 1 else a[(e - 1) // 2] for e in range(len(a) * 2)]
        result = self.reduction(temp, self.modul)
        return result

    def power(self, arr, n):
        result = [1]

        while ((int(''.join([str(e) for e in n]), 2)) != 0):
            if (self.bit_and(n)):
                result = self.multiplication(result, arr)
                n = self.addition(n, [1])
            else:
                arr = self.square(arr)
                n = self.shift_right(n, 1)
        return result

    def inverse_element(self, a):
        result = a
        temp = a
        m = self.m

        for i in range(1, m - 1, 1):
            temp = self.square(temp)
            result = self.multiplication(temp, result)

        result = self.square(result)
        return result

    def Trace(self, a):
        trace = a
        temp = a
        m = self.m

        for i in range(1, m, 1):
            temp = self.square(temp)
            trace = self.addition(trace, temp)

        for i in range(0, len(trace)):
            if trace[i] != 0:
                trace = trace[i:]
                break
        return trace
