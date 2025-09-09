# Python code below
import json
import os


#  her code
# def encodeString(stringVal):
#     encodedList = []
#     prevChar = None
#     count = 0
#     for char in stringVal:
#         if prevChar != char and prevChar is not None:
#             encodedList.append((prevChar, count))
#             count = 0
#         prevChar = char
#         count = count + 1
#     encodedList.append((prevChar, count))
#
#     print(encodedList)
#     return encodedList

def encodeString(stringVal):
    encodedString = []
    # Your code goes here.
    prevChar = None
    count = 1
    for char in stringVal:
        # print('char: ' + char)
        if char != prevChar:
            # print('prevChar: ' + str(prevChar))
            # print('count: ' + str(count))
            if prevChar is not None:
                currentChar = prevChar
                # print("currentChar: " + str(currentChar))
                if char != currentChar:
                    encodedString.append((prevChar, count))
                    prevChar = char
                    count = 1
            else:
                prevChar = char
        else:
            count +=1
    # handle last characters
    # print("at the end, last char: " + str(prevChar) + " and count: " + str(count))
    encodedString.append((prevChar, count))
    return encodedString

def decodeString(encodedList):
    # Your code goes here.
    return "".join(str(key * value) for key, value in encodedList)


# The filename that will be passed to this function
# is 10_04_challenge_art.txt
# def encodeFile(filename, newFilename):
#     # Your code goes here.
#     # inFile = open(filename, 'r')
#     # outFile = open(newFilename, 'w')
#     # Better file handling with context manager
#     # REMEMBER: using 'with' will automatically close the file for you!
#     with open(filename, 'r') as inFile:
#         encodedString = encodeString(inFile.read())
#
#     #  try to make data smaller
#     encodedString = [f'{char}|{count}' for char, count in encodedString]
#
#     with open(newFilename, 'w') as outFile:
#         # outFile.write(json.dumps(encodedString))
#         # more compact version:
#         outFile.write('~'.join(encodedString))
#
#
#     #  send in each line of the file to encodeString
#     # outputArray = []
#     # for line in inFile:
#     #     encodedLine = encodeString(line)
#     #     outputArray.extend(encodedLine)
#     #
#     # print('encodedString: ', outputArray)
#     # outFile.write(json.dumps(outputArray))
#     # inFile.close()
#     # outFile.close()
#
#
# def decodeFile(filename):
#     # Your code also goes here.
#     # inFile = open(filename, 'r')
#     # encodedString = json.loads(inFile.read())
#     # outString = decodeString(encodedString)
#     # inFile.close()
#     # return outString
#
# #     better file handling with context manager
#     with open(filename, 'r') as inFile:
#         encodedString = inFile.read()
#
#     pairs = encodedString.split('~')
#     pairs = [p.split('|') for p in pairs]
#     pairs = [{p[0], int(p[1])} for p in pairs]
#     return decodeString(pairs)
#     # return decodeString(json.loads(encodedString))


# Byte solution - should make it even smaller
def encodeFile(filename, newFilename):
    with open(filename, 'r') as inFile:
        encodedString = encodeString(inFile.read())

    output = bytearray()

    for item in encodedString:
        # Character byte
        output.extend(item[0].encode('utf-8'))
        # Integer count byte
        output.extend(item[1].to_bytes(1, 'big'))

    with open(newFilename, 'wb') as outFile:
        # Write bytes to file
        outFile.write(output)

def decodeFile(filename):
    with open(filename, 'rb') as f:
        data = f.read()
#         Split data into pairs
    bytePairs = [data[i:i+2] for i in range(0, len(data), 2)]
    encodedList = []
    for bytePair in bytePairs:
        encodedList.append((bytePair[:1].decode('utf-8'), int.from_bytes(bytePair[1:], 'big')))
    return decodeString(encodedList)

# class Answer:
#     def __init__(self, value):
#         self.value = value
#
#     def display(self):
#         print(f"The answer is: {self.value}")
# Test
original_filesize = os.path.getsize("10_04_challenge_art.txt")
print(f'Original file size: {original_filesize}')
encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')

new_filesize = os.path.getsize("10_04_challenge_art_encoded.txt")
print(f'New file size: {new_filesize}')
decoded = decodeFile('10_04_challenge_art_encoded.txt')
print(decoded)