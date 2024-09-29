def decrypt_vigenere(ciphertext, keyword):
    diff = len(ciphertext) % len(keyword)
    if diff != 0:
        key = (keyword * (len(ciphertext) // len(keyword))) + keyword[:diff]
    else:
        key = (keyword * (len(ciphertext) // len(keyword)))
    ciphertext = list(ciphertext)
    key = list(key)
    x = ''
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) - (ord(key[i]) - 65) < 65:
            x = x + chr((ord(ciphertext[i]) - (ord(key[i]) - 65) + 90) - 64)
        elif ord(ciphertext[i]) > 64 and ord(ciphertext[i]) < 91:
            x = x + chr((ord(ciphertext[i]) - (ord(key[i]) - 65)))
        elif ord(ciphertext[i]) - (ord(key[i]) - 97) < 97:
            x = x + chr((ord(ciphertext[i]) - (ord(key[i]) - 97) + 122) - 96)
        else:
            x = x + chr(ord(ciphertext[i]) - (ord(key[i]) - 97))
    plaintext = x
    return plaintext