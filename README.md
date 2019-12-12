# YARPG - Yet Another Random Password Generator

As a paranoid infosec person, I don't trust anyone. Not even their password generators, especially since I can't look at their code. So I wrote my own random password generator. And I still want to improve my Python skills. 

Enter yarpg.py - Yet Another Random Password Generator

This uses the secure random generator random.SystemRandom()

### Usage
```
yarpg.py [-h|-L <length> -n <numofpasswords> -t [complex|alphanumeric]]
```
```-h``` Display the help.

```-L``` Length of the password. This is the total length of the password. The default is 15, which is much stronger than 8 and usually accepted in most password systems. There is no maximum--create as big of a password as you want.

```-n``` Number of passwords generators. By default, three password are generated at a time. However, there are times you want to have more than that generated at a time (e.g. sysadmins creating multiple accounts at once), so you can use this.

```-t``` Type of password(s) generated. There are two types currently: complex and alphanumeric. Some password implementations are stupid and don't let you use special characters, thus, this choice. You have three options: alphanumeric, complex, and both. The default type is complex, so if you want alphanumeric or both, you will need to define that.

### Examples

Run the defaults, assuming the python executable is at /usr/bin.
```
$ /usr/bin/python yarpg.py
Complex Password #1: ?TjXIgX5~=!"$o;
Complex Password #2: 'g]LLJ}a[u,F}:+
Complex Password #3: =Cv[u&}~5y$ZM[n

```
Display the help.
```
$ /usr/bin/python yarpg.py -h
usage: yarpg.py [-L pwlength -n numberofpw -t type]

Default number of passwords: 3 
Default length of each password: 15 characters
Default password type: complex

```
Generate 1 alphanumeric password that's 15 characters.
```
$ /usr/bin/python yarpg.py -t alphanumeric
Alphanumeric Password #1: EhoqLSmFAZvSFaC
Alphanumeric Password #2: PI5EPFDticGWvdq
Alphanumeric Password #3: L2tQ3eFQ2HnlSzY
```
Generate 5 complex passwords that's 20 characters.
```
$ /usr/bin/python yarpg.py -L 20 -n 5 
Complex Password #1: ODT9%bu<3n!8SXw${8#-
Complex Password #2: >R0xgbJf4P:=K=^1h}b;
Complex Password #3: Y8X{\6TJ?s44({Wo\x;'
Complex Password #4: k.Dr<}$mnIbax"!L)?Sj
Complex Password #5: ve@36I@pa8=7+lxpp-ND

```

### Environments Tested

This works on both Mac OS X 10.9.5, Debian Linux, OpenBSD, and Windows 7. Please feel free to test in additonal environments and let me know if you have issues. I'd like for this to be as portable as possible.

### To Do
* Make it so you can pick which special characters you can include since most password systems still have some level of limitation or suckage.
* Better error checking. 
* Test on additional platforms
* Try different libraries like argparse to expand the code
