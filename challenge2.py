from challenge1 import hex2bin


def Xor(byte1, byte2):
    """
    byte1: byte_array\n
    byte2: byte_array\n
    Xor([0,0,0,0], [0,0,0,1]) => [0,0,0,1]\n
    Returns the XOR combination from two byte arrays, with length x.\n
    0000 ^ 0001 => 0001
    0 XOR 0 => 0
    0 XOR 1 => 1
    1 XOR 0 => 1
    1 XOR 1 => 0
    """
    res = []
    for i in range(len(byte1)):
        res.append(byte1[i] ^ byte2[i])
    return res


def XorHexstrings(buffer1 , buffer2):
    """
    buffer1: hex_string
    buffer2: hex_string
    XorHexstrings("1c", "4B") => [[0, 1, 0, 1], [0, 1, 1, 1]]
    This functions takes to equal lenght buffers and computes the XOR of them, after hex decoding. 
    Returns the binairy representation of the the strings.
    """
    if len(buffer1) == len(buffer2):
        buffer1 = hex2bin(buffer1)
        buffer2 = hex2bin(buffer2)

        result = []
        for i in range(len(buffer1)):
            result.append(Xor(buffer1[i], buffer2[i]))

        return result
    else:
        print("No two equal lenght buffers")


def bin2decimal(byte):
    """
    byte: [0,0,0,0] (4-byte array)
    BinairtoDecimal([0,0,0,0]) => 0
    Returns an integer number for a 4-bit binairy representation.
    """
    #Start at 0 and increment it every each iteration
    result = 0
    column = 8
    for bit in byte:
        result = result + (column * bit)
        column = column /2
    return int(result) #To convert the result from float to an integer, because of the division

def bin2hex(byte_array):
    """
    byte_array: byte_array\n
    hex2bin([[0,0,1,1],[1,1,1,1]]) => "3f"\n
    Takes a 4-bit byte array and converts it to its hexadecimal representation.    
    """
    result = ""

    for byte in byte_array:
        tmp = bin2decimal(byte)

        #Convert the integer to a letter
        if tmp == 10:
            tmp = "a"
        elif tmp == 11:
            tmp = "b"
        elif tmp == 12:
            tmp = "c"
        elif tmp == 13:
            tmp = "d"
        elif tmp == 14:
            tmp = "e"
        elif tmp == 15:
            tmp = "f"
        else:
            tmp = str(tmp) #Converts i.e. 3 to "3"
        
        result += tmp

    return result


if __name__ == "__main__":
    buffer1 = "1c0111001f010100061a024b53535009181c"
    buffer2 = "686974207468652062756c6c277320657965"

    solution = "746865206b696420646f6e277420706c6179"

    if bin2hex(XorHexstrings(buffer1, buffer2)) == solution:  
        print("Yeah, challenge 2 is correct!!!!")
    else:
        print("Wrong!!!")