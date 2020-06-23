# Create-Simple-Wordlists
I made this python code to create some simple wordlists, i was doing [this room](https://tryhackme.com/room/passwordcracking) in tryhackme and started writing this python code to help me in it, but then i got i little exited with it and made it do more than it needed.

It is really simple and can only make simple wordlists, here's how you can use it:
```
python3 create-wordlist.py -i 3 -a abcde > out.txt
```
In this example there will be created a file named out.txt that has all possible iterations of the letters abcde up to 3 characters long.

## Options

* -i choose how many characters long can be the iterations of the alphabet

* -a choose the alphabet (the default is "01234567890")

* -f chose the files to open and then the program will then print the words of the first file folowed by the words of the second file and will keep going on for all files ...

* -t instead of printing the words of the files in order, it will print all possible iterations between the words of the files

* -m chose a string to print in each word

* -e chose between 4 different modes to be arranged the string from -m, the alphabet iterations from -i and -a and the output of files from -f:
   - 1 string then files then alphabet
   - 2 alphabet then files then string
   - 3 alphabet then files then alphabet
   - 4 string then files then string
   
None of the options are mandatory
