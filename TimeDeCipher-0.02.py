#------------------#
###Time De-Cipher###
#------------------#
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

print("""Time De-Cipher 0.02
by Lilith""" + "\n" * 3)

#abcdefghijklmnopqrstuvwõäöüxyABCDEFGHIJKLMNOPQRSTUVWÕÄÖÜ1234567890.,:;!\/"#¤%&()=?*-_ @£$

CharList = {
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h",
    8 : "i",
    9 : "j",
    10 : "k",
    11 : "l",
    12 : "m",
    13 : "n",
    14 : "o",
    15 : "p",
    16 : "q",
    17 : "r",
    18 : "s",
    19 : "t",
    20 : "u",
    21 : "v",
    22 : "w",
    23 : "õ",
    24 : "ä",
    25 : "ö",
    26 : "ü",
    27 : "x",
    28 : "y",
    29 : "A",
    30 : "B",
    31 : "C",
    32 : "D",
    33 : "E",
    34 : "F",
    35 : "G",
    36 : "H",
    37 : "I",
    38 : "J",
    39 : "K",
    40 : "L",
    41 : "M",
    42 : "N",
    43 : "O",
    44 : "P",
    45 : "Q",
    46 : "R",
    47 : "S",
    48 : "T",
    49 : "U",
    50 : "V",
    51 : "W",
    52 : "Õ",
    53 : "Ä",
    54 : "Ö",
    55 : "Ü",
    56 : "1",
    57 : "2",
    58 : "3",
    59 : "4",
    60 : "5",
    61 : "6",
    62 : "7",
    63 : "8",
    64 : "9",
    65 : "0",
    66 : ".",
    67 : ",",
    68 : ":",
    69 : ";",
    70 : "!",
    71 : "\\",
    72 : "/",
    73 : "\"",
    74 : "#",
    75 : "¤",
    76 : "%",
    77 : "&",
    78 : "(",
    79 : ")",
    80 : "=",
    81 : "?",
    82 : "*",
    83 : "-",
    84 : "_",
    85 : " ",
    86 : "\n",
    87 : "@",
    88 : "£",
    89 : "$",
    90 : "“",
    91 : "”",
    92 : "z",
    93 : "’",
    94 : "„"
}


#----------------------------------------#
###Open Ciphered File and Read Contents###
#----------------------------------------#

CipheredFile = input("What is the name of the file you want to decipher?\n>")
#Getting time#
Time = CipheredFile[:12]

CiphFile = open(CipheredFile, "r")
CiphedText = CiphFile.read()
#print(CiphedText)

#--------------------------#
###UnSalt Ciphed Contents###
#--------------------------#

deciphedLength = len(CiphedText)
UnSaltA = 50
UnsaltB = UnSaltA + 12

while UnsaltB < deciphedLength:
    CiphedText = CiphedText[:UnSaltA] + CiphedText[UnsaltB:]
    UnSaltA += 40
    UnsaltB = UnSaltA + 12

print(type(CiphedText))
input()
#---------------------#
###Decipher Contents###
#---------------------#

deciphedLength = len(CiphedText)
deciphed = ""
ReaderCount = 0
#print(deciphedLength)

while ReaderCount < deciphedLength:

    if CiphedText[ReaderCount] == "+":
        deciphed = deciphed[:-1]
        ReaderCount += 2
        deciphed += " "
    else:
        deciphed += str(CiphedText[ReaderCount])
        ReaderCount += 1

deciphedList = deciphed.split()
print(deciphedList)
input()
deciphedListLength = len(deciphedList)
ListCount = 0
while ListCount < deciphedListLength:
    a = int(deciphedList[ListCount])
    a -= int(Time)
    deciphedList[ListCount] = a
    ListCount += 1

print(deciphedList)
input()


DeCipheredText = ""
a = 0
while a < deciphedListLength:
    CiphChar = CharList[deciphedList[a]]
    DeCipheredText += CiphChar
    a += 1

cls()
print(DeCipheredText)
print("")
PrintPrompt = input("Do you want that in a textfile(y/n)?\n>")
while True:
    if PrintPrompt == "y":
        NAME = Time + "_DeCiphered.txt"
        f = open(NAME, "w")
        f.write(DeCipheredText)
        f.close()
        print("Your deciphered text is saved in " + NAME)
        print("Bye!")
        break
    elif PrintPrompt == "n":
        print("Bye")
        break
    else:
        PrintPrompt = input("No such option, try again (y/n).")


exit()
