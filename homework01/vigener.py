def encrypt_vigenere(plaintext, keyword):
    diff = len(plaintext) % len(keyword)
    if diff != 0:
        key = (keyword * (len(plaintext) // len(keyword))) + keyword[:diff]
    else:
        key = (keyword * (len(plaintext) // len(keyword)))
    plaintext = list(plaintext)
    key = list(key)
    x = ''
    for i in range(len(plaintext)):
        if ord(plaintext[i]) + (ord(key[i]) - 97) > 122:
            x = x + chr((ord(plaintext[i]) + (ord(key[i]) - 97) - 122) + 96)
        elif ord(plaintext[i]) + (ord(key[i]) - 97) > 96 and ord(plaintext[i]) + (ord(key[i]) - 97) < 123:
            x = x + chr((ord(plaintext[i]) + (ord(key[i]) - 97)))
        elif ord(plaintext[i]) + (ord(key[i]) - 65) > 90:
            x = x + chr((ord(plaintext[i]) + (ord(key[i]) - 65) - 90) + 64)
        else: x = x + chr(ord(plaintext[i]) + (ord(key[i]) - 65))
    ciphertext = x
    return ciphertext