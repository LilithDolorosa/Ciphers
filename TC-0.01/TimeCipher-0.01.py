#---------------#
###Time Cipher###
#---------------#
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

print("""Time Cipher 0.01
by Lilith""" + "\n" * 3)

#CharList = "abcdefghijklmnopqrstuvwõäöüxyABCDEFGHIJKLMNOPQRSTUVWÕÄÖÜ1234567890.,:;!\/"#¤%&()=?*-_ "

CharList = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7,
    "i" : 8,
    "j" : 9,
    "k" : 10,
    "l" : 11,
    "m" : 12,
    "n" : 13,
    "o" : 14,
    "p" : 15,
    "q" : 16,
    "r" : 17,
    "s" : 18,
    "t" : 19,
    "u" : 20,
    "v" : 21,
    "w" : 22,
    "õ" : 23,
    "ä" : 24,
    "ö" : 25,
    "ü" : 26,
    "x" : 27,
    "y" : 28,
    "A" : 29,
    "B" : 30,
    "C" : 31,
    "D" : 32,
    "E" : 33,
    "F" : 34,
    "G" : 35,
    "H" : 36,
    "I" : 37,
    "J" : 38,
    "K" : 39,
    "L" : 40,
    "M" : 41,
    "N" : 42,
    "O" : 43,
    "P" : 44,
    "Q" : 45,
    "R" : 46,
    "S" : 47,
    "T" : 48,
    "U" : 49,
    "V" : 50,
    "W" : 51,
    "Õ" : 52,
    "Ä" : 53,
    "Ö" : 54,
    "Ü" : 55,
    "1" : 56,
    "2" : 57,
    "3" : 58,
    "4" : 59,
    "5" : 60,
    "6" : 61,
    "7" : 62,
    "8" : 63,
    "9" : 64,
    "0" : 65,
    "." : 66,
    "," : 67,
    ":" : 68,
    ";" : 69,
    "!" : 70,
    "\\" : 71,
    "/" : 72,
    "\"" : 73,
    "#" : 74,
    "¤" : 75,
    "%" : 76,
    "&" : 77,
    "(" : 78,
    ")" : 79,
    "=" : 80,
    "?" : 81,
    "*" : 82,
    "-" : 83,
    "_" : 84,
    " " : 85,
    "\n" : 86,
    "@" : 87,
    "£" : 88,
    "$" : 89,
    "“" : 90,
    "”" : 91,
    "z" : 92,
    "’" : 93,
    "„" : 94
}


CharListLength = len(CharList)
#print(CharListLength - 1)

#--------------------------------#
###Get time, make it an integer###
#--------------------------------#
from datetime import datetime
DateTime = str(datetime.now().time())
##Get rid of shit
trash = ".:"
for char in trash:
    DateTime = DateTime.replace(char, "")
#print(DateTime)

#---------------------#
###Read the contents###
#---------------------#
FileName = input("Enter the file name:\n>")
OpenFile = open(str(FileName), "r")
Text = OpenFile.read()
#print(Text)

#------------------#
###Cipher content###
#------------------#
print(DateTime)

TextSplitList = list(Text)
#print(TextSplitList)
TextSplitListLenght = len(TextSplitList)
#print(TextSplitListLenght) --> 42
CiphedText = ""
a = 0
while a < TextSplitListLenght:
    CiphNum = CharList[TextSplitList[a]]
    CiphNum += int(DateTime)
    CiphedText += str(CiphNum)
    CiphedText += "0+0"
    a += 1

print(Text)
#print(CiphedText)

###WORK IN PROGRESS###

#plusCounter = 0
#for plus in CiphedText:
#    if plusCounter == 4:
#        plusCounter = 0
#
#    if plus == "+":
#        plusCounter += 1
#    else:
#        pass


#----------------#
###Create salts###
#----------------#
from random import randint
SaltIndex = int(DateTime) * 2
#print(SaltIndex)
SaltIndex = [int(d) for d in str(SaltIndex)]
#print("SaltIndex = " + str(SaltIndex))
SaltLength = 0
SaltList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while SaltLength < 12:
    SaltList[SaltLength] = randint(100000000000,999999999999)
    SaltLength += 1
    #print(SaltList)

#-----------------------#
###Salt chiphered text###
#-----------------------#


#-------------------------------------------#
###Add Time to ciphered file###
#-------------------------------------------#


#-------------------------#
###Create chiphered file###
#-------------------------#
CreateFilePrompt = input("Create file(y/n)?\n>")
while CreateFilePrompt in ["y", "n"]:
    if CreateFilePrompt == "y":
        CipheredFileName = str(DateTime) + FileName + "_Ciphed.txt"
        CiphedFile = open(CipheredFileName, "w")
        CiphedFile.write(CiphedText)
        CiphedFile.close()
        break

    elif CreateFilePrompt == "n":
        print("No file was created. Closing.")
        print("Bye!")
        break


    else:
        CreateFilePrompt = input("No such option. Try again (y/n).")


exit()
