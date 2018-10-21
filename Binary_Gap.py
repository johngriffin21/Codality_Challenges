#Write a function:

#    def solution(N)

#that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap. 


#For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of
#length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.


def string_maker(X):                    #Create a string of zeros that we can match
    list_zeros = '1' + '0' * X + '1'    #Needs a one before and behind it
    return list_zeros


def solution(N):
    binary_number = str(bin(N))[2:]     #Convert N to binary using pythons built in
    len_binary = len(binary_number)

    for number_of_zeros in reversed(range(len_binary)): #Doing this in reverse should increase efficiency
        li = string_maker(number_of_zeros)
        if li in binary_number:
            return number_of_zeros
    return 0                               #No amount of zeros have been matches

#Task score = 100%
