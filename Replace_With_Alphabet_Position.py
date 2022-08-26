def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha():
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')


print(alphabet_position("The sunset sets at twelve o' clock."))
