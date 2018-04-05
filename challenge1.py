#Support method for hex2bin
def decimal2bin(number, bit_system):
    """
    number: int\n
    decimal2bin(15) => [1,1,1,1]\n 
    Returns an n-bit representation of an integer, the maximum value depends on the bit system you fill in.
    """
    #Start with the binary representation of 0
    result = []
    tmp = bit_system
    while tmp >= 1:
        result.append(0)
        tmp /= 2

    bin_index = 0

    #Number represents the state of the binary sequence
    column = bit_system
    while number > 0:
        if number >= column:
            number -= column
            result[bin_index] = 1
        bin_index += 1
        column /= 2
    return result

def contains(sequence, value):
    """
    sequence: iterable
    value: number
    contains([1,2,3,4], 3) => True
    Returns True when a sequence contains a certain value, else False.
    """
    for i in range(len(sequence)):
        if sequence[i] == value: return True
    return False

def find(sequence, value):
    """
    array: iterable
    value: number
    find([1,2,3,4], 3) => 2
    Returns the index from the element in the sequence.
    """
    for i in range(len(sequence)):
        if sequence[i] == value: return i
    return -1

def hex2bin(_hex):
    """
    hex: string\n
    hex2bin("3F") => [[0,0,1,1],[1,1,1,1]]\n
    Takes hexadecimal number and converts it to a 4-bit
    two dimensional byte array. Where evey byte represents one hexadecimal number.
    4F => 0100 1111
    """
    #Start with an empty array, this will be filled
    result = []

    #Itterate over every character in the string
    for i in range(len(_hex)):
        #Store the current character of the hex string in a variable
        tmp = _hex[i]

        #Convert the letter to an integer  
        hex_set = ["a", "b", "c", "d", "e", "f"]
        if contains(hex_set, tmp):
            tmp = find(hex_set, tmp)+10
        else: 
            tmp = int(tmp) #Python can convert i.e. "3" to 3


        #Convert the hexadecimal code to binairy
        result.append(decimal2bin(tmp, 8))

    return result

#Support method for bin2base64
def BinairtoDecimal(byte, bit_system):
    """
    byte: [0,0,0,0,0,0] (n-byte array)
    BinairtoDecimal([0,0,0,0,0,0]) => 0
    Returns an integer number for a n-bit binairy representation.
    """
    #Start at 0 and increment it every each iteration
    result = 0
    column = bit_system
    for bit in byte:
        result = result + (column * bit)
        column = column /2
    return int(result) #To convert the result from float to an integer, because of the division
        
def bin2base64(byte_array):
    """
    byte_array: [[[0, 0, 0, 1], [1, 0, 1, 0]], [[0, 0, 1, 0], [1, 1, 1, 1]], [[1,0, 0, 0], [1, 0, 1, 1]]]\n
    bin2base64([[[0, 0, 0, 1], [1, 0, 1, 0]], [[0, 0, 1, 0], [1, 1, 1, 1]], [[1,0, 0, 0], [1, 0, 1, 1]]]) => Gi+L \n 
    Returns a base64 character set from a binairy representation, the input from this function is
    equals to the output of hex2bin(). 
    """
    #This functions is build in 5 steps, the steps to go from a 8-bit byte array to base64 are:
    #1. Divide the bytes in pieces of 6
    #2. At zero's to the bits until the total can be divided by 6
    #3. Convert the individual bytes to decimal numbers
    #4. Look in a base64 character table for matching character, the index in the table corresponds with the decimal number
    #5. (optional) Make one string for prety printing ;)

    #Example
    # 0001 0101 1100 1010
    #Step 1: 000101 010110 01010
    #Step 2: 000101 010110 010100 (added 1 zero)
    #Step 3: 5      22     20
    #Step 4: E      V      T
    #Step 5: EVT


    #In code it becomes:

    #Step 1
    #Put al bits in a single array
    bits = []
    for byte in byte_array:
            for bit in byte:
                bits.append(bit)

    #Step 2
    while len(bits) % 6 > 0:
        bits.append(0)

    #Step 3
    #Iterate over the bits in pieces of 6
    result = []
    for i in range(0, len(bits), 6):
        result.append(BinairtoDecimal(bits[i:i+6], 32))
    
    #Step 4
    #This array represents the base64 table, the index in the array corresponds with the correct character
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    #For each character replace the number with the corresponding character
    for c in range(len(result)):
        result[c] = base64[result[c]]

    #Step 5
    #Convert the array of characters to one single string
    prety_string = ""
    for letter in result:
        prety_string += letter

    return prety_string #You can return result to see the differents


if __name__ == "__main__":
    #Convert hex to base64
               #The string:
    encoded = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
                #Should produce:
    solution = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    #So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

    if bin2base64(hex2bin(encoded)) == solution:
        print("Yeah answer is correct!!!!")
    else:
        print("Wrong!!!!!!")

    #Cryptopals rule: Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.