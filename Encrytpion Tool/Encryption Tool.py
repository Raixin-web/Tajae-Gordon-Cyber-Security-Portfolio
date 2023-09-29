

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            shifted = chr((ord(char) - 65 + shift) % 26 + 65)
            result += shifted

        elif char.islower():
            shifted = chr((ord(char) - 97 + shift) % 26 + 97)
            result += shifted

        else:
            result += char
    return result


encrypted_text = encrypt("Hello, World!", 3)
print(encrypted_text)