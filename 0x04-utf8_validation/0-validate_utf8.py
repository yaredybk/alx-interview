#!/usr/bin/python3
"""UTF-8 Validation."""


def validUTF8(data):
    """UTF-8 Validation.

    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data,
    therefore use the 8 least significant bits of each integer

    Return: True if data is a valid UTF-8 encoding, else return False
    """
    if len(data) == 0:
        return False
    valid = True
    cursor = 0
    length = len(data)
    while valid and cursor < length:
        val = data[cursor]
        # print(f'->{val}:{bin(val)}')
        if val < 127:
            cursor += 1
            continue
        val &= 0xFF
        shift = 0
        while val & (0b10000000 >> shift):
            # print(f'shift={shift}')
            if shift > 3:
                valid = False
                break
            shift += 1
        if not valid:
            break
        if shift == 0:
            cursor += 1
            continue
        if shift == 1 or shift > 4:
            # print('if shift == 1 or shift > 4:')
            valid = False
            break
        if (cursor + shift) > length:
            # print(f'{cursor}:{shift}:{length}')
            # print('if (cursor + shift) > length:')
            valid = False
            break
        for i in range(shift - 1):
            # print(f'shift2:{cursor + i + 1}')
            val2 = data[cursor + i + 1] & 0xFF
            if (val2 & 0b11000000) != 0b10000000:
                # print(f'E:cont:{val2}:{bin(val2)}')
                valid = False
                break
        cursor += shift
    return valid
