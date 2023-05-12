from caesar_cipher import CaesarCipher
import string


def test_caesar_cipher():
    # Test 1
    sentence = "Hello, World!"
    shift = 4
    characters = string.ascii_letters
    cipher = CaesarCipher(sentence, shift, characters)
    encrypted = cipher.encrypt()
    assert encrypted == "Lipps, asvph!"
    decrypted = CaesarCipher(encrypted, shift, characters).decrypt()
    assert decrypted == sentence

    # Test 2
    sentence = "To be or not to be, that is the question"
    shift = -15
    characters = string.ascii_letters
    cipher = CaesarCipher(sentence, shift, characters)
    encrypted = cipher.encrypt()
    assert encrypted == "EZ MP Zc YZe eZ MP, eSLe Td eSP bfPdeTZY"
    decrypted = CaesarCipher(encrypted, shift, characters).decrypt()
    assert decrypted == sentence

    # Test 3
    sentence = "14*(3x + 2) – 4 = 2*(x - 1) + x"
    shift = 95
    characters = string.ascii_lowercase + string.digits + string.punctuation + ' '
    cipher = CaesarCipher(sentence, shift, characters)
    encrypted = cipher.encrypt()
    assert encrypted == "<?ca>.zdz=bz–z?zlz=ca.zfz<bzdz."
    decrypted = CaesarCipher(encrypted, shift, characters).decrypt()
    assert decrypted == sentence
