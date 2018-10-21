def string_maker(X):
    list_zeros = '1' + '0' * X + '1'
    return list_zeros


def solution(N):
    binary_number = str(bin(N))[2:]  # Convert N to binary using pythons built in
    len_binary = len(binary_number)

    for t in reversed(range(len_binary)): #doing this in reverse should increase efficiency
        li = string_maker(t)
        if li in binary_number:
            return t
    return 0                               #no amount of zeros have been matches

