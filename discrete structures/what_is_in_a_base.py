base2 = 'Ol'
base8 = 'O1234567'
base10 = 'O123456789'
base16 = 'O123456789ABCDEF'
duodecimal = 'O123456789AB'
aliens = 'ᐁᐃᐄᐅᐆᐇᐉᐊᐋᐖᐛᐯᐱᐲᐳᐴᐵᐷᐸᐹᑀᑂᑅᑇᑈᑌᑍᑎᑏᑐᑑᑒᑓᑔᑕᑖᑝᑟᑢᑤᑥᑫᑭᑮᑯᑰᑱᑲᒉᒋᒌᒍᒏᒐᒒᒕᒗᒘᒝ'
babylonian = ['𒊹𒊹','𒊹𒑰','𒊹𒈫','𒊹𒐈','𒊹𒐉','𒊹𒐊','𒊹𒐋','𒊹𒑂','𒊹𒑄','𒊹𒑆','𒌋𒊹','𒌋𒑰','𒌋𒈫','𒌋𒐈','𒌋𒐉','𒌋𒐊','𒌋𒐋','𒌋𒑂','𒌋𒑄','𒌋𒑆','𒎙𒊹','𒎙𒑰','𒎙𒈫','𒎙𒐈','𒎙𒐉','𒎙𒐊','𒎙𒐋','𒎙𒑂','𒎙𒑄','𒎙𒑆','𒌍𒊹','𒌍𒑰','𒌍𒈫','𒌍𒐈','𒌍𒐉','𒌍𒐊','𒌍𒐋','𒌍𒑂','𒌍𒑄','𒌍𒑆','𒑩𒊹','𒑩𒑰','𒑩𒈫','𒑩𒐈','𒑩𒐉','𒑩𒐊','𒑩𒐋','𒑩𒑂','𒑩𒑄','𒑩𒑆','𒑪𒊹','𒑪𒑰','𒑪𒈫','𒑪𒐈','𒑪𒐉','𒑪𒐊','𒑪𒐋','𒑪𒑂','𒑪𒑄','𒑪𒑆']

# DO NOT MODIFY THIS FUNCTION! IT IS USED INSTEAD OF assert TO TEST YOUR CODE
def expectEqual(a, b):
    if a != b: print('FAIL expected:', b, ' got:', a)

def stringToInt(number, base):
    # initialize variables
    base_len = len(base)
    num_len = len(number)
    base_digit_len = len(base[0])

    # accounts for bases with multiple characters per digit
    if base_digit_len > 1:
        # generate a list of digits based on the digit length and change num_len to reflect it
        number = [number[i : i + base_digit_len] for i in range(0, num_len, base_digit_len)]
        num_len = num_len // base_digit_len

    ret_list = list()
    rev_num = reversed(number)

    # compare all characters in the string to the base string, and append the index
    for n in rev_num:
        for b in range(0, base_len):
            if n == base[b]:
                ret_list.append(b)
    
    ret_int = 0

    # find d^n, loop through the list, and add integer 
    for n in range(num_len):
        digit = base_len ** n
        the_int = ret_list[n] * digit
        ret_int += the_int

    # return the integer
    return ret_int

expectEqual(stringToInt('2O', base10), 20)
expectEqual(stringToInt('31337', base10), 31337)
expectEqual(stringToInt('lOlOO', base2), 20)
expectEqual(stringToInt('llllOlOOllOlOOl', base2), 31337)
expectEqual(stringToInt('2O', base8), 16)
expectEqual(stringToInt('31337', base8), 13023)
expectEqual(stringToInt('2O', base16), 32)
expectEqual(stringToInt('31337', base16), 201527)
expectEqual(stringToInt('ᑀ', aliens), 20)
expectEqual(stringToInt('𒎙𒊹', babylonian), 20)
expectEqual(stringToInt('𒊹𒈫𒊹𒐈', babylonian), 123)
expectEqual(stringToInt('bb','ab'), 3)

def intToString(integer, base):

    # initialize variables
    base_len = len(base)
    base_digit_len = len(base[0])
    the_number = integer
    original_string = ''

    # loop through the number and add to the string
    while (the_number > 0):
        # take a digit, add it to string, and move to next digit
        digit = base[the_number % base_len]
        original_string = original_string + digit
        the_number = the_number // base_len

    # accounts for bases with multiple characters per digit
    if base_digit_len > 1:
        # generate a list of digits based on the digit length
        return_list = [original_string[i : i + base_digit_len] for i in range(0, len(original_string), base_digit_len)]

        # reverse the list and create a string out of it
        return_list = reversed(return_list)
        return_string = ''.join(return_list)
    else:
        # reverse the string
        return_string = original_string[::-1]

    # return the string
    return return_string

expectEqual(intToString(1230,base10), '123O')
expectEqual(intToString(31337,base10), '31337')
expectEqual(intToString(123,base2), 'llllOll')
expectEqual(intToString(31337,base2), 'llllOlOOllOlOOl')
expectEqual(intToString(31337,base8), '75151')
expectEqual(intToString(123,base8), '173')
expectEqual(intToString(123,duodecimal), 'A3')
expectEqual(intToString(31337,duodecimal), '16175')
expectEqual(intToString(123,base16), '7B')
expectEqual(intToString(31337,base16), '7A69')
expectEqual(intToString(123,aliens), 'ᐄᐇ')
expectEqual(intToString(123,babylonian), '𒊹𒈫𒊹𒐈')
expectEqual(intToString(51,babylonian), '𒑪𒑰')
expectEqual(intToString(7,'ab'),'bbb')

def add(a,b, base):
    
    # turn both strings into integers
    a_int = stringToInt(a, base)
    b_int = stringToInt(b, base)

    # add the two values
    return_int = a_int + b_int

    # turn the int back into a string
    return_string = intToString(return_int, base)
    
    # return the string
    return return_string

expectEqual(add('123','123',base10), '246')
expectEqual(add('98','123',base10), '221')
expectEqual(add('lOl','lO',base2), 'lll')
expectEqual(add('lOlO','lO',base2), 'llOO')
expectEqual(add('123','123',base8), '246')
expectEqual(add('4563','77',base8), '4662')
expectEqual(add('123','123',duodecimal), '246')
expectEqual(add('123','123',base16), '246')
expectEqual(add('4563','78',base16), '45DB')
expectEqual(add('ᐄᐇ','ᑅᑇᑈ',aliens), 'ᑅᑌᑐ')
expectEqual(add('ᒍᒏᒐ','ᒍᒏᒐ',aliens), 'ᐃᑯᑱᑲ')
expectEqual(add('ᒒᒕᒗᒘᒝ','ᑅᑇᑈ',aliens), 'ᒒᒗᑀᑅᑇ')
expectEqual(add('𒊹𒑰𒊹𒈫𒊹𒐈','𒊹𒑰𒊹𒈫𒊹𒐈',babylonian), '𒊹𒈫𒊹𒐉𒊹𒐋')
expectEqual(add('𒑪𒑄','𒑪𒑆',babylonian), '𒊹𒑰𒑪𒑂')