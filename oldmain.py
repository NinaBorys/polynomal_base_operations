#! /usr/bin/python3.3
from polynomal_base_library import *


def main():

    first_str = '10111001101111101010101011001100111110101001100110100110010001001001101010100111101100001010100110001110000001101011010011011011010110110010111001000100101011100011111110110110100100100010101'

    second_str = '10010110010011011000000110001110110111100110001110000010010110001000100110110110101010100111101100101100010000100111000111110110110010001111011101100001100010111010110101011110100110001110000'

    n_str = '11110111011011010101001100011000000011110001100100000010001100011000011000001001110110011101000010010011111100110100000100110101011000100001001010001001011100010011111100100101110000111000100'

    first_array = [int(z) for z in first_str]
    second_array = [int(z) for z in second_str]
    n_array = [int(z) for z in n_str]
    # print(first_array)
    # print(second_array)

    m = 191
    mod = (m + 1) * [0]
    mod[0] = 1
    mod[m] = 1
    mod[182] = 1

    polynom = Polynom(mod, m)
    # print(polynom.power(first_array, second_array))
    print(polynom.reduction(first_array, mod))

    print("=========== Addition ==============\n")
    k = (polynom.addition(first_array, second_array))

    for i in range(0, len(k)):
        if k[i] != 0:
            k = k[i:]
            break

    ttt = '00101111111100110010101101000010001001001111101000100100000111000001001100010001000110101101001010100010010001001100010100101101100100111101100100100101001001011001001011101000000010101100101'

    correct = [int(z) for z in ttt]

    for i in range(0, len(correct)):
        if correct[i] != 0:
            correct = correct[i:]
            break

    # print(correct)
    # print('')
    # print(k)

    print(correct == k)

    print("=========== Multiplication ==============\n")

    mm = (polynom.multiplication(first_array, second_array))
    # print(mm)

    print('')
    mm_r = '01110001001111100111111111001000010110110001011100010011011100100001100011001001101011101100011101011001011111100100000010010010001010101001001011100111011001111000010010100110111101011010010'

    correct1 = [int(z) for z in mm_r]
    # print(correct1)

    for i in range(0, len(correct1)):
        if correct1[i] != 0:
            correct1 = correct1[i:]
            break

    print(correct1 == mm)

    print("=========== Square ==============\n")

    scr_arr = polynom.square(first_array)

    # print(scr_arr)

    scr_str = '01100111111000011110110111010110111011100110110011011000010110000101010101100100010000011110001101100100001111000001001010111000110010110110011011001100000101010110010100001000111011110111011'
    correct2 = [int(z) for z in scr_str]

    for i in range(0, len(correct2)):
        if correct2[i] != 0:
            correct2 = correct2[i:]
            break

    print(correct2 == scr_arr)

    print("=========== Power ==============\n")

    pow_arr = polynom.power(first_array, n_array)
    pow_ans_str = '11010101110100010011001101010001010111001000110000011101010110001000100101010100000011000111101011000010110110111101011000000000111110100000000101011100110101111111000111110010110010110010001'
    correct3 = [int(z) for z in pow_ans_str]

    for i in range(0, len(correct3)):
        if correct3[i] != 0:
            correct3 = correct3[i:]
            break

    print(correct3 == pow_arr)

    print("=========== Inverced element ==============\n")

    inv_arr = polynom.inverse_element(first_array)
    print('')

    inv_ans_str = '00010001101111010110110000111011010001101001111001010110101110110101101011111011100100110000111101000011110011001110111000001111011010010100111111111011111000001010111101101010111001111011011'
    correct4 = [int(z) for z in inv_ans_str]

    for i in range(0, len(correct4)):
        if correct4[i] != 0:
            correct4 = correct4[i:]
            break
    print(correct4 == inv_arr)

    print("=========== Trace of element ==============\n")

    tr_ar = polynom.Trace(first_array)

    print(tr_ar)
    print('')

if __name__ == '__main__':
    main()
