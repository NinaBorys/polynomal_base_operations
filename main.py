#! /usr/bin/python3

from polynomal_base_library import Polynom


def main():
    s1 = '1011100110111111'
    s2 = '1001011001001101'
    m = 191
    x = Polynom(m, s1)
    y = Polynom(m, s2)
    z = x + y
    print(z)

if __name__ == '__main__':
    main()
