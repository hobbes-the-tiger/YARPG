# YARPG - Yet Another Random Password Generator

As a paranoid infosec person, I don't trust anyone. Not even their password generators, especially since I can't look at their code. So I wrote my own random password generator. And I still want to improve my Python skills. 

Enter yarpg.py - Yet Another Random Password Generator

This uses the secure random generator random.SystemRandom()

###Usage
```
yarpg.py [-h|-L <length> -n <numofpasswords> -t [complex|alphanumberic|all]]
```
```-h``` Display the help.

```-L``` Length of the password. This is the total length of the password. The default is 8, which is ridiculously weak, so you should change this.

```-n``` Number of passwords generators. The default is 3, no more, no less (Monty Python and the Holy Grail reference for those who didn't get it). Seems like a reasonable number. Feel free to use any integer you'd like. Using zero is silly, and the program will complain if you try that.

```-t``` Type of password(s) generated. There are two types currently: complex and alphanumeric. Some password implementations are stupid and don't let you use special characters, thus, this choice. You have three options: alphanumeric, complex, and both. The default type is both, so you don't need to put that in unless you like to type a lot.

###Examples

Run the defaults, assuming the python executable is at /usr/bin.
```
$ /usr/bin/python yarpg.py
Complex Password #1: w`$ml0BZ
Alphanumberic Password #1: xqXsmTIY
Complex Password #2: pr$"C<En
Alphanumberic Password #2: imfhAmot
Complex Password #3: VjQ&*h;7
Alphanumberic Password #3: ljdSZN3J
```
Display the help.
```
$ /usr/bin/python yarpg.py -h
usage: yarpg.py -L pwlength -n numberofpw -t type.

Default passwords: 3
Default Length: 8
Default Type: both alphanumeric and complex
```
Generate 1 alphanumeric password that's 8 characters.
```
$ /usr/bin/python yarpg.py -n 1 -t alphanumeric
Alphanumberic Password #1: D1ZaWVP7
```
Generate 5 complex passwords that's 20 characters.
```
$ /usr/bin/python yarpg.py -L 20 -n 5 -t complex
Complex Password #1: 'q@:+M^x,Q~:m8S<.rBP
Complex Password #2: HA=o}!NOp9E5`S(fL]$C
Complex Password #3: F<r(bYv!QDY!7&${n~:c
Complex Password #4: <d19$AQC]u[~EX+?@yfC
Complex Password #5: 5MdCZ,X`dg{p,\tW/$=O
```

###Environments Tested

This works on both Mac OS X 10.9.5 and Debian Linux. Please feel free to test in additonal environments and let me know if you have issues. I'd like for this to be as portable as possible.

###To Do
* Make it so you can pick which special characters you can include since most password systems still have some level of limitation or suckage.
* Better error checking. 
* Test on additional platforms
