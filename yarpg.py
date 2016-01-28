#!/usr/bin/python
#
# yarpg.py - Yet Another Random Password Generator
#
# Usage: yarpg.py -L <length> -n <numofpasswords> -t [complex|alphanumeric]
#

import getopt
import random
import string
import sys

# Set the default values
DEFAULT_PWLEN=15
DEFAULT_NUMPW=3
TYPE_ALPHA = 1
TYPE_COMPLEX = 2
TYPE_BOTH = 3
RNG = random.SystemRandom()

USAGE_TEXT = """usage: yarpg.py -L pwlength -n numberofpw -t type
Default number of passwords: 3
Default length of each password: 15 characters
Default password type: complex"""

def generate_random_pw(charset, pwlen):
  return "".join([RNG.choice(charset) for _ in xrange(pwlen)])

def main(argv):
  numpw = DEFAULT_NUMPW
  pwlen = DEFAULT_PWLEN
  typeflag = TYPE_COMPLEX

  try:
    opts, args = getopt.getopt(argv, "hL:n:t:",["help", "pwlen=", "numpw=", "pwtype"])
  except getopt.GetoptError:
    sys.exit(USAGE_TEXT)

  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print USAGE_TEXT
      sys.exit(0)
    elif opt in ("-L", "--passwordlength"):
      pwlen = int(arg)
    elif opt in ("-n", "--number"):
      numpw = int(arg)
      if numpw < 1:
        sys.exit("Oops. You need at least one password to generate.")
    elif opt in ("-t", "--type"):
       typeflag = str(arg)
       if typeflag in "alphanumeric":
          typeflag = TYPE_ALPHA
       elif typeflag in "complex":
          typeflag = TYPE_COMPLEX
       elif typeflag in "both":
          typeflag = TYPE_BOTH
       else:
          sys.exit("Oops. Type " + typeflag + " is not a valid option.")

  for x in range(numpw):
    if typeflag == TYPE_ALPHA:
      print "Alphanumeric Password #" + str(x+1) + ": " + generate_random_pw(string.ascii_letters + string.digits, pwlen)
    elif typeflag == TYPE_COMPLEX:
      print "Complex Password #" + str(x+1) + ": " + generate_random_pw(string.ascii_letters + string.digits + string.punctuation, pwlen)
    elif typeflag == TYPE_BOTH:
      print "Alphanumeric Password #" + str(x+1) + ": " + generate_random_pw(string.ascii_letters + string.digits, pwlen)
      print "Complex Password #" + str(x+1) + ": " + generate_random_pw(string.ascii_letters + string.digits + string.punctuation, pwlen)

if __name__ == "__main__":
  main(sys.argv[1:])
