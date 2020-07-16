alfa = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890áéíóú,.*();?\n:"

alfa_dictionary = dict([ (x[1],x[0]) for x in enumerate(alfa) ])

# print(alfa_dictionary)

def get_next_num(num, width):
    if num+width > len(alfa_dictionary):
        return get_next_num(num - len(alfa_dictionary) , width)
    else:
        return num + width




def get_last_num(num, width):
    if num - width < 0:
        return get_last_num(len(alfa_dictionary) + num , width)
    else:
        return num - width




def encrypt(value, width):
    encrypt_word = ""
    for char in value:
        next_char_num = get_next_num(alfa_dictionary[char], width)
        # print(next_char_num)
        # asumimos que la clave es primero ya que al declarar bnuestro alfa_dictionary invertimos valores ejm : {"a":1}
        for word, key in alfa_dictionary.items():
            if next_char_num == key:
                encrypt_word += word
                break
        # print(encrypt_word)
    return encrypt_word





def decrypt(value, width):
    decrypt_word = ""
    for char in value:
        last_char_num = get_last_num(alfa_dictionary[char], width)
        for word, key in alfa_dictionary.items():
            if last_char_num == key:
                decrypt_word += word
                break
    return decrypt_word


encrypt_word = encrypt("cUCHARA",4)

texto_desencriptado = decrypt("gYGLEVE", 4)

print(encrypt_word)
print(texto_desencriptado)

