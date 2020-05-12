import sys

def argParser():
    #parser used for detecting integer as first cmd line argument
    try:
        num = sys.argv[1]
        if num.isdigit() and int(sys.argv[1]) > 0:
            return True
        else:
            raise
    except:
        return False

def dumbText(input, maxLineLen):
    #worker functions that goes throught whole input /all words/ and divides them accordingly
    lineBuffer = []
    newLineFlag = False
    paragraphFlag = False
    separator = ' '

    for word in wordYielder(input):
        wordNoSpaces = word.strip()
        if word == '\n' and newLineFlag:
            paragraphFlag = True
        elif not wordNoSpaces:
            continue
        else:
            if newLineFlag and paragraphFlag: #last line of paragraph
                if lineBuffer:
                    print(separator.join(lineBuffer))
                newLineFlag = False
                paragraphFlag = False
                lineBuffer.clear()
                print()
            if len(separator.join(lineBuffer)) + len(wordNoSpaces) + 1 <= maxLineLen: #fits into a line
                lineBuffer.append(wordNoSpaces)
            elif len(word) >= maxLineLen:
                addCorrectSpaces(lineBuffer, maxLineLen)
                print(wordNoSpaces)
                lineBuffer.clear()
            else: #last dumb
                addCorrectSpaces(lineBuffer, maxLineLen)
                lineBuffer.clear()
                lineBuffer.append(wordNoSpaces)

            if word.endswith('\n'):
                newLineFlag = True
                continue
    if lineBuffer:
        print(separator.join(lineBuffer))

def wordYielder(file):
    #loops over parameter 'file' and yiels words
    for line in file:
        for word in line.split(' '):
            yield word

def addCorrectSpaces(line, maxLen):
    #fills holes between words with spaces
    if len(line) == 1:
        print(line[0])
        return
    elif not line:
        return
    else:
        toAdd = maxLen - len(''.join(line))

        #spaces = [''] * len(line)

        while(toAdd > 0):
            for i,word in enumerate(line[:-1]):
                if toAdd:
                    line[i] += ' '
                    toAdd -= 1
                else:
                    break
            if not toAdd:
                break
        print(''.join(line))

if __name__ == "__main__":
    if argParser():
        dumbText(sys.stdin, int(sys.argv[1]))
    else:
        print("Error")