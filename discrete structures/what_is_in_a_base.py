"""
what_is_in_a_base.py

exercises involving number bases.

author: christopher romo
"""


def expect_equal(a: any, b: any) -> None:
    """
    compares two values and prints a message if they are not equal.

    args:
        a (any): the first value.
        b (any): the second value.
    """

    if a != b:
        print("FAIL expected:", b, " got:", a)


def string_to_int(number: str, base: str) -> int:
    """
    converts a string representation of a number in a given base to an integer.

    args:
        number (str): the string representation of the number.
        base (str): the base string representing the digits of the base.

    returns:
        int: the integer representation of the number.
    """

    # initialize variables
    base_len = len(base)
    num_len = len(number)
    base_digit_len = len(base[0])

    # accounts for bases with multiple characters per digit
    if base_digit_len > 1:
        # generate a list of digits based on the digit length and change
        # num_len to reflect it
        number = [
            number[i : i + base_digit_len] for i in range(0, num_len, base_digit_len)
        ]
        num_len = num_len // base_digit_len

    ret_list = list()
    rev_num = reversed(number)

    # compare all characters in the string to the base string, and append the
    # index
    for n in rev_num:
        for b in range(0, base_len):
            if n == base[b]:
                ret_list.append(b)

    ret_int = 0

    # find d^n, loop through the list, and add integer
    for n in range(num_len):
        digit = base_len**n
        the_int = ret_list[n] * digit
        ret_int += the_int

    # return the integer
    return ret_int


def int_to_string(integer: int, base: str) -> str:
    """
    converts an integer to its string representation in a given base.

    args:
        integer (int): the integer to convert.
        base (str): the base string representing the digits of the base.

    returns:
        str: the string representation of the number in the given base.
    """

    # initialize variables
    base_len = len(base)
    base_digit_len = len(base[0])
    the_number = integer
    original_string = ""

    # loop through the number and add to the string
    while the_number > 0:
        # take a digit, add it to string, and move to next digit
        digit = base[the_number % base_len]
        original_string = original_string + digit
        the_number = the_number // base_len

    # accounts for bases with multiple characters per digit
    if base_digit_len > 1:
        # generate a list of digits based on the digit length
        return_list = [
            original_string[i : i + base_digit_len]
            for i in range(0, len(original_string), base_digit_len)
        ]

        # reverse the list and create a string out of it
        return_list = reversed(return_list)
        return_string = "".join(return_list)
    else:
        # reverse the string
        return_string = original_string[::-1]

    # return the string
    return return_string


def add(a: str, b: str, base: str) -> str:
    """
    adds two numbers represented as strings in a given base.

    args:
        a (str): the first number as a string.
        b (str): the second number as a string.
        base (str): the base string representing the digits of the base.

    returns:
        str: the sum of the two numbers as a string in the given base.
    """

    # turn both strings into integers
    a_int = string_to_int(a, base)
    b_int = string_to_int(b, base)

    # add the two values
    return_int = a_int + b_int

    # turn the int back into a string
    return_string = int_to_string(return_int, base)

    # return the string
    return return_string


def main() -> None:
    """exercises involving number bases."""

    # originally a jupyter notebook exercise

    base2 = "Ol"
    base8 = "O1234567"
    base10 = "O123456789"
    base16 = "O123456789ABCDEF"
    duodecimal = "O123456789AB"
    aliens = "ᐁᐃᐄᐅᐆᐇᐉᐊᐋᐖᐛᐯᐱᐲᐳᐴᐵᐷᐸᐹᑀᑂᑅᑇᑈᑌᑍᑎᑏᑐᑑᑒᑓᑔᑕᑖᑝᑟᑢᑤᑥᑫᑭᑮᑯᑰᑱᑲᒉᒋᒌᒍᒏᒐᒒᒕᒗᒘᒝ"
    babylonian = [
        "𒊹𒊹",
        "𒊹𒑰",
        "𒊹𒈫",
        "𒊹𒐈",
        "𒊹𒐉",
        "𒊹𒐊",
        "𒊹𒐋",
        "𒊹𒑂",
        "𒊹𒑄",
        "𒊹𒑆",
        "𒌋𒊹",
        "𒌋𒑰",
        "𒌋𒈫",
        "𒌋𒐈",
        "𒌋𒐉",
        "𒌋𒐊",
        "𒌋𒐋",
        "𒌋𒑂",
        "𒌋𒑄",
        "𒌋𒑆",
        "𒎙𒊹",
        "𒎙𒑰",
        "𒎙𒈫",
        "𒎙𒐈",
        "𒎙𒐉",
        "𒎙𒐊",
        "𒎙𒐋",
        "𒎙𒑂",
        "𒎙𒑄",
        "𒎙𒑆",
        "𒌍𒊹",
        "𒌍𒑰",
        "𒌍𒈫",
        "𒌍𒐈",
        "𒌍𒐉",
        "𒌍𒐊",
        "𒌍𒐋",
        "𒌍𒑂",
        "𒌍𒑄",
        "𒌍𒑆",
        "𒑩𒊹",
        "𒑩𒑰",
        "𒑩𒈫",
        "𒑩𒐈",
        "𒑩𒐉",
        "𒑩𒐊",
        "𒑩𒐋",
        "𒑩𒑂",
        "𒑩𒑄",
        "𒑩𒑆",
        "𒑪𒊹",
        "𒑪𒑰",
        "𒑪𒈫",
        "𒑪𒐈",
        "𒑪𒐉",
        "𒑪𒐊",
        "𒑪𒐋",
        "𒑪𒑂",
        "𒑪𒑄",
        "𒑪𒑆",
    ]

    # task 1

    # Implement a number parser. The function should take a string
    # representation of a number and a base and convert the string into a
    # Python integer. Note: in all deliverables, hard-coded components may help
    # you pass tests, but they will receive very few points. For example, the
    # character 'O' always has the value 0, but we will not look favorably on
    # code which says something like if character=='O' : value = 0. Your code
    # should infer the value of the character 'O' based on its position in the
    # string base2, etc.

    expect_equal(string_to_int("2O", base10), 20)
    expect_equal(string_to_int("31337", base10), 31337)
    expect_equal(string_to_int("lOlOO", base2), 20)
    expect_equal(string_to_int("llllOlOOllOlOOl", base2), 31337)
    expect_equal(string_to_int("2O", base8), 16)
    expect_equal(string_to_int("31337", base8), 13023)
    expect_equal(string_to_int("2O", base16), 32)
    expect_equal(string_to_int("31337", base16), 201527)
    expect_equal(string_to_int("ᑀ", aliens), 20)
    expect_equal(string_to_int("𒎙𒊹", babylonian), 20)
    expect_equal(string_to_int("𒊹𒈫𒊹𒐈", babylonian), 123)
    expect_equal(string_to_int("bb", "ab"), 3)

    # task 2

    # Given an integer and a base, generate the string representation of number
    # in given base.

    expect_equal(int_to_string(1230, base10), "123O")
    expect_equal(int_to_string(31337, base10), "31337")
    expect_equal(int_to_string(123, base2), "llllOll")
    expect_equal(int_to_string(31337, base2), "llllOlOOllOlOOl")
    expect_equal(int_to_string(31337, base8), "75151")
    expect_equal(int_to_string(123, base8), "173")
    expect_equal(int_to_string(123, duodecimal), "A3")
    expect_equal(int_to_string(31337, duodecimal), "16175")
    expect_equal(int_to_string(123, base16), "7B")
    expect_equal(int_to_string(31337, base16), "7A69")
    expect_equal(int_to_string(123, aliens), "ᐄᐇ")
    expect_equal(int_to_string(123, babylonian), "𒊹𒈫𒊹𒐈")
    expect_equal(int_to_string(51, babylonian), "𒑪𒑰")
    expect_equal(int_to_string(7, "ab"), "bbb")

    # task 3

    # In the real world, we would just take the functions we just created
    # above, combine them with the existing addition facilities in the computer
    # and compute sums of numbers represented in any base. But, this isn't the
    # real world at all. This is Discrete Structures. Implement a generic
    # function that performs addition in-base (with carries and everything).

    expect_equal(add("123", "123", base10), "246")
    expect_equal(add("98", "123", base10), "221")
    expect_equal(add("lOl", "lO", base2), "lll")
    expect_equal(add("lOlO", "lO", base2), "llOO")
    expect_equal(add("123", "123", base8), "246")
    expect_equal(add("4563", "77", base8), "4662")
    expect_equal(add("123", "123", duodecimal), "246")
    expect_equal(add("123", "123", base16), "246")
    expect_equal(add("4563", "78", base16), "45DB")
    expect_equal(add("ᐄᐇ", "ᑅᑇᑈ", aliens), "ᑅᑌᑐ")
    expect_equal(add("ᒍᒏᒐ", "ᒍᒏᒐ", aliens), "ᐃᑯᑱᑲ")
    expect_equal(add("ᒒᒕᒗᒘᒝ", "ᑅᑇᑈ", aliens), "ᒒᒗᑀᑅᑇ")
    expect_equal(add("𒊹𒑰𒊹𒈫𒊹𒐈", "𒊹𒑰𒊹𒈫𒊹𒐈", babylonian), "𒊹𒈫𒊹𒐉𒊹𒐋")
    expect_equal(add("𒑪𒑄", "𒑪𒑆", babylonian), "𒊹𒑰𒑪𒑂")

    print("If no failures were printed, all tests passed!")


if __name__ == "__main__":
    main()
