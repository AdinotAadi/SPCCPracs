KEYWORDS = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]
keywordsFound = []
PUNCTUATIONS = ["(", ")", "[", "]", "{", "}", ",", ".", ":", ";"]
punctuationsFound = []
OPERATORS = ["+", "-", "*", "/", "%", "=", "++", "--", "+=", "-=", "*=", "/=", "<", ">", "!", "!="]
operatorsFound = []
identifiersFound = []
numbersFound = []
tokensFound = []

filePath = input("Enter the file path: ")
with open(filePath, "r") as f:
    lines = f.readlines()
    arr = []
    for line in lines:
        arr.extend(line.split())
    for token in arr:
        tokensFound.append(token)
    print("Tokens found:", tokensFound)
    for token in tokensFound.copy():
        if token in KEYWORDS:
            keywordsFound.append(token)
            tokensFound.remove(token)
        elif token in PUNCTUATIONS:
            punctuationsFound.append(token)
            tokensFound.remove(token)
        elif token.isnumeric():
            numbersFound.append(token)
            tokensFound.remove(token)
        elif token in OPERATORS:
            operatorsFound.append(token)
            tokensFound.remove(token)
        else:
            identifiersFound.append(token)
            tokensFound.remove(token)
    print("Keywords found:", len(set(keywordsFound)), "\n", set(keywordsFound))
    print("Punctuations found:", len(set(punctuationsFound)), "\n", set(punctuationsFound))
    print("Operators found:", len(set(operatorsFound)), "\n", set(operatorsFound))
    print("Identifiers and Functions found:", len(set(identifiersFound)), "\n", set(identifiersFound))
    print("Numbers found:", len(set(numbersFound)), "\n", set(numbersFound))
