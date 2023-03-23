import string
import commons

alphabet = string.ascii_lowercase
numbers = '0123456789'

def convertLetterToNewLetter(letter, moveNLetters):
    letterIndex = alphabet.find(letter)

    if (letterIndex < 0):
        return letter
    
    newIndex = (letterIndex + moveNLetters) % len(alphabet)
    
    return alphabet[newIndex]

def convertLetterToNewNumber(number, moveNLetters):
    letterIndex = numbers.find(number)

    if (letterIndex < 0):
        return number
    
    newIndex = (letterIndex + moveNLetters) % len(numbers)
    
    return numbers[newIndex]

def encryptString(string, moveNLetters):
    lowerstring = commons.convertStringToLowerCase(string)

    newString = ''

    for letter in lowerstring:
        if (letter.isnumeric()):
            newString += convertLetterToNewNumber(number=letter, moveNLetters=moveNLetters)
        else:
            newString += convertLetterToNewLetter(letter=letter, moveNLetters=moveNLetters)

    return newString