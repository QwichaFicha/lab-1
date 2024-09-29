def ENCRYPT_caesar(plaintext):
    x = ''
    for i in plaintext:
        if (ord(i) > 64) and (ord(i) < 88):
            x = x + (chr(ord(i) + 3))
        elif (ord(i) > 87) and (ord(i) < 91):
            x = x + (chr(ord(i) - 23))
        elif (ord(i) > 96) and (ord(i) < 120):
            x = x + (chr(ord(i) + 3))
        elif (ord(i) > 119) and (ord(i) < 123):
            x = x + (chr(ord(i) - 23))
        else: x = x + i
    ciphertext = x

    return ciphertext

def decrypt_caesar(ciphertext):
    x = ''
    for i in ciphertext:
        if (ord(i) > 67) and (ord(i) < 91):
            x = x + (chr(ord(i) - 3))
        elif (ord(i) > 64) and (ord(i) < 68):
            x = x + (chr(ord(i) + 23))
        elif (ord(i) > 99) and (ord(i) < 123):
            x = x + (chr(ord(i) - 3))
        elif (ord(i) > 96) and (ord(i) < 100):
            x = x + (chr(ord(i) + 23))
        else:
            x = x + i
    plaintext = x
    return plaintext