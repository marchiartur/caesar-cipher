import file
import caesarCipher

def main():
    filename = 'file.txt'
    
    filecontent = file.readFile(filename=filename)
    
    encrypted = caesarCipher.encryptString(filecontent, 4)
    
    outputFilename = 'encrypted.txt'

    file.writeFile(outputFilename, encrypted)
        


if __name__ == '__main__':
    main()