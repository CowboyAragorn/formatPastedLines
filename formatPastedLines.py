#! /usr/bin/python3
#formatPastedLines.py converts copied values separated by lines into various formats
#useful for copying text from internet to make lists
import pyperclip, sys, re

rawText = pyperclip.paste()
#Gives you a single string, was using for pasting into javascript
def rawToStr():
    formattedStr = '"{0}"'.format('","'.join(rawText.splitlines()))
    pyperclip.copy(formattedStr)
    
    print('Formatted String Copied to Clipboard')
    print('See formatted string below:\n')
    print(formattedStr)
    return formattedStr

    #example:
    #'''
    #feelings = '''Accepting
    #Open
    #Calm
    #Centered
    #'''
    #prints "feelings","open","Calm","Centered"

#returns info in list format
def rawToList():
    formattedString = (','.join(rawText.splitlines()))
    li = list(formattedString.split(","))
    while "" in li:
        li.remove("")
    return li


#Remove numbers:
def rmNums(format_li):
    numRegex = re.compile(r'^(\d)+(.|-)?')
    for i in range(len(format_li)):
        format_li[i] = re.sub(numRegex, '', format_li[i])
        format_li[i] = format_li[i].strip()
    return format_li
    #ex:
    #1. Mammal
    #2. Fish
    #3. Bird
    # Becomes ["Mammal","Fish",Bird"]

#CLI interaction
if len(sys.argv) < 2:
    print('''------------------------------
Usage:

formatPastedLines.py rawToStr - converts copied values separated by lines
    & returns str of comma separated vals in quotes for list
formatPastedLines.py rawToList - converts copied values separated
    by a line to a list
formatPastedLines.py rmNumsList - Removes leading numbers from copied items
    and returns list of copied values
-------------------------------------------''')
    
elif sys.argv[1] == "rawToStr":
    rawToStr()
elif sys.argv[1] == 'rawToList':
    list = rawToList()
    #pyperclip.copy(list)
    print('Formatted List Copied to Clipboard')
    print('See formatted list below:')
    print(list)
elif sys.argv[1] == 'rmNumsList':
    li = rmNums(rawToList())
    #technically returns as str due to pyperclip limitation, but you can paste it
    #into another file and it will be accepted as a list due to formatting
    pyperclip.copy(str(li))
    print('Formatted List Copied to Clipboard')
    print('See formatted list below:')
    print(li)

    
    
