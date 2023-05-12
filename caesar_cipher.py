import itertools


class CaesarCipher:
    """
    Initialize the CaesarCipher class with a given sentence, shift value, and set of characters.
    Parameters:
        sentence (str): The sentence to be encrypted.
        shift (int): The shift value to be used for encryption.
        characters (str): The set of all characters that can appear in the sentence.
    """
    def __init__(self, sentence, shift, characters):
        self.sentence = sentence
        self.characters = characters
        self.shift = shift
        # Ensuring that the shift value is non-negative in order to use it with itertools.islice()
        if self.shift < 0:
            self.shift = len(self.characters) - abs(self.shift) % len(self.characters)
        # Creating a dictionary to store the encryption key and its inverse
        self.key = {}
        self.inv_key = {}
        # Creating a cycle of characters to iterate over
        cycle_characters = itertools.cycle(self.characters)
        # Getting new indices for characters starting at index shift
        new_indices = itertools.islice(cycle_characters, self.shift, None)
        for character in self.characters:
            new_index = next(new_indices)
            self.key[character] = new_index
            self.inv_key[new_index] = character

    def __return_new_sentence(self, key):
        """Private method that returns the new sentence after encryption or decryption"""
        return ''.join([key.get(character, character) for character in self.sentence])

    def encrypt(self):
        """Method that encrypts the sentence and returns the encrypted text"""
        return self.__return_new_sentence(self.key)

    def decrypt(self):
        """Method that decrypts the sentence and returns the decrypted text"""
        return self.__return_new_sentence(self.inv_key)
