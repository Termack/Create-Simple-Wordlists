import sys
import time
alphabet = "0123456789"
start_time = time.time()

ite = 0
files = []
message = ""
allit = False
mode = 1

helpm = '''
    Usage: python3 create-wordlist.py [Options]

    Options
        -h show  this help message
        -i chose the number of letters of the alphabet
        -f chose the files to open and put in the beggining of each string
        -t put all possible combinations of the files instead of putting it in order
        -m chose the message
        -a chose the alphabet used for bruteforcing, default = "0123456789"
        -e change the mode (Default 1):
            1 = message in the beggining and alphabet in the end
            2 = alphabet in the beggining and message in the end
            3 = alphabet in the beggining and the end
            4 = message in the beggining and the end
        
    Examples'''
args =  sys.argv
if(len(args) <= 1):
    print(helpm)
for i in range(len(args)):
    if args[i] == "-h":
        print(helpm)
    elif args[i] == "-i":
        try:
            ite = int(args[i+1])
        except:
            print("The argument following -i must be a int")
    elif args[i] == "-m":
        if i < len(args)-1:
            message = args[i+1]
    elif args[i] == "-a":
        if i < len(args)-1:
            alphabet = args[i+1]
    elif args[i] == "-t":
        allit = True
    elif args[i] == "-e":
        try:
            mode = int(args[i+1])
            if mode < 0 or mode > 4:
                raise Exception()
        except:
            print("The argument following -e must be a int between 1 and 4")
    elif args[i] == "-f":
        try:
            j = 1
            while(i+j <= len(args)-1 and not args[i+j][0] == "-"):
                with open(args[i+j]) as f:
                    files.append(f.read())
                j+=1
        except:
            print("Could not open " + args[i+j])

def printCombinations(fileresult,string,it):
    if it <= 0:
        for l in fileresult:
            if mode == 1:
                print(message+l+string)
            elif mode == 2:
                print(string+l+message)
            elif mode == 3:
                print(string+l+string)
            elif mode == 4:
                print(message+l+message)
        return
    for i in alphabet:
        printCombinations(fileresult,string + i,it-1)

def fileIterations(result,string,filenum):
    if(filenum >= len(files)):
        result += string + "\n"
        return result
    for l in files[filenum].splitlines():
        result = fileIterations(result,string+l,filenum+1)
    return result

if(allit):
    import itertools
    fileit = []
    for x in itertools.permutations(files):
        files = x
        for l in fileIterations("","",0).splitlines():
            fileit.append(l)
else:
    fileit = fileIterations("","",0).splitlines()

if(ite>0):
    for i in range(1,ite+1):
        printCombinations(fileit,"",i)
else:
    printCombinations(fileit,"",ite)