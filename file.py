def readFile(filename):    
    with open(filename, 'r', encoding='utf-8') as f:
        fileContent = f.read()
    
    return fileContent

def writeFile(filename, string):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(string)
        
        return True
    except:
        raise Exception('error to write in file')