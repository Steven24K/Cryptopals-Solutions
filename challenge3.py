from challenge1 import hex2bin
from challenge1 import bin2base64
from challenge1 import decimal2bin
from challenge1 import BinairtoDecimal
from challenge2 import Xor



def SingleByteXOR(hex_string):
    """
    hex_string: string
    SingleByteXOR("1b") => [(0, '\x1b'), (1, '\x1a'), (2, '\x19'), (3, '\x18'), (4, '\x1f'), (5, '\x1e'),..., ... etc.
    Returns a tuple that contains the encryption key and the ASCII representation from the hex encode string
    XOR'ed by a single 8-bit byte. The function tries every possible combination from 0000 0000 to 1111 1111 (0-255).
    """

    #Start with an empty byte array, and fill it with the binairy representation of the hex string.
    #Because the hex2bin function returns 4-bit bytes, we first need to combine two 4-bit bytes to make one 8-bit byte.
    #So [[0,0,0,1], [0,1,0,1] becomes [0,0,0,1,0,1,0,1].
    _bytes = []
    for i in range(0,len(hex_string), 2):
        tmp = hex2bin(hex_string[i:i+2])
        r = []
        for y in tmp:
            for x in y:
                r.append(x)
        _bytes.append(r)

    #XOR every byte against the key starting from 0 and increment until 255
    key = 0
    decrypted = []
    while key <= 255:
        answer = []
        for byte in _bytes:
            answer.append(Xor(decimal2bin(key, 128), byte))
        
        #Convert the XOR'ed bytes to ASCII
        characters = ""
        for a in answer:
            characters += str(chr(BinairtoDecimal(a,128)))
        
        decrypted.append((key,characters))
        key += 1
    return decrypted




if __name__ == "__main__":
    #Single-byte XOR cipher

    #The hex encoded string:
    encoded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    #has been XOR'd against a single character. Find the key, decrypt the message.
    
    #You can do this by hand. But don't: write code to do it for you.

    #How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. 
    #Evaluate each output and choose the one with the best score.

    #The key is 88, the decrypted message is: "Cooking MC's like a pound of bacon"
    print(SingleByteXOR(encoded)[88][1])
