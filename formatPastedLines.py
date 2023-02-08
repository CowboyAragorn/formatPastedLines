#! /usr/bin/python3
#formatPastedLines.py converts copied values separated by lines into various formats
#useful for copying text from internet to make lists
import pyperclip, sys

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
def rmNums():
    print()
    

#CLI interaction
if len(sys.argv) < 2:
    print('''------------------------------
Usage:

formatPastedLines.py rawToStr - converts copied values separated by lines
    & returns str of comma separated vals in quotes for list
formatPastedLines.py rawToList - converts copied values separated
    by a line to a list
-------------------------------------------''')
    
elif sys.argv[1] == "rawToStr":
    rawToStr()
elif sys.argv[1] == 'rawToList':
    list = rawToList()
    #pyperclip.copy(list)
    print('Formatted List Copied to Clipboard')
    print('See formatted list below:')
    print(list)

    
    
