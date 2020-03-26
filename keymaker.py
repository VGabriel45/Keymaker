from string import ascii_lowercase as alphabet


def get_alphabet_list():
    a_to_z = []
    for index, letter in enumerate(alphabet):
        a_to_z.append(letter)
    return a_to_z


def shift_characters(word, shift):
    result = []
    for char in word:
        for index, letter in enumerate(alphabet):
            # print(index, letter)
            if letter == char:
                if index + shift >= 25:
                    x = (index + shift) - index - (25-index)
                    # print(alphabet[x - 1], end=' ')
                    result.append(alphabet[x - 1])
                else:
                    # print(alphabet[index + shift], end=' ')
                    result.append(alphabet[index + shift])
    return ''.join(result)


# print(shift_characters('abby', 5))


def pad_up_to(word, shift, n):
    shifted = [word]
    for _ in range(5):
        shifted_word = shift_characters(word, 5)
        shifted.append(shifted_word)
        word = shifted_word
    shifted = ''.join(map(str, shifted))
    return shifted[:n]


# print(pad_up_to('abb', 5, 11))


def abc_mirror(word):
    mirrored_word = []
    a_to_z = get_alphabet_list()
    for char in word:
        for index, letter in enumerate(a_to_z):
            if letter == char:
                mirrored_letter = a_to_z[-(index+1)]
                mirrored_word.append(mirrored_letter)
    return ''.join(mirrored_word)


# print(abc_mirror('morpheus'))


def create_matrix(word1, word2):
    values = []
    for char in word2:
        for index, letter in enumerate(alphabet):
            if char == letter:
                values.append(shift_characters(word1, index))
    return values


# print(create_matrix('mamas', 'papas'))


def zig_zag_concatenate(matrix):
    # Try 1:
    # count = 0
    # matrix1 = matrix[0][0] + matrix[1][0] + matrix[2][0] + matrix[3][0] + \
    #     matrix[3][1] + matrix[2][1] + matrix[1][1] + matrix[0][1] + \
    #     matrix[0][2] + matrix[1][2] + matrix[2][2] + matrix[3][2]

    # Try 2:
    # for i in range(len(matrix)):
    #     lst.append(matrix[count][0])
    #     count += 1
    #     if count > 3:
    #         for i in range(len(matrix)):
    #             count -= 1
    #             lst.append(matrix[count][1])
    #             if count == 0:
    #                 for i in range(len(matrix)):
    #                     lst.append(matrix[count][2])
    #                     count += 1

    # Try 3:
    result = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix)):
            result.append(matrix[j][i])
    result = result[:4] + list(reversed(result[4:8])) + result[8:]
    # result = result[:len(result)//3] + list(reversed(result[len(result)//3:(len(result)//3) * 2])) + result[(len(result)//3) * 2:] # [4:8]

    return result


# print(zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl']))


def rotate_right(word, nr_of_rotations):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    list_of_letters = []
    for letter in word:
        list_of_letters.append(letter)
    lenght = len(list_of_letters)

    list_of_letters = list_of_letters[-(lenght + nr_of_rotations) %
                                      lenght:] + list_of_letters[0:-(lenght+nr_of_rotations) % lenght]
    return list_of_letters


# print(rotate_right('abcdefgh', 3))


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    pass


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    pass


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


# if __name__ == '__main__':
#     name = input("Enter your name! ").lower()
#     print(f'Your key: {hash_it(name)}')
