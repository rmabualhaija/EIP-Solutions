# Compute the parity of a 64 bit word
# parity counts the number of 1's in the
# binary representation of the word where 1 would represent
# an odd parity (e.g. 11100) and 0 represents an even parity
# e.g (1010)


def compute_parity(num):
    num_ones = 0

    while num:
        if num & 1:
            num_ones += 1
        num >>= 1

    print(num_ones)

    return num_ones & 1


print(compute_parity(100))
